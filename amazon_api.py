#!/usr/bin/env
#-*- coding: utf-8 -*-
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
from easelenium.firefox_selenium import Firefox
from selenium.common.exceptions import NoSuchElementException
import time
#-----------------------------------------------------------------------------------------------------------------------------------------------------------


class AmazonAPI:

    def __init__(self,settings):
        '''This class would do the work of scraping Amazon pages.''' 
        #The basic information.
        self.base_url = settings.BASE_URL
        self.search_term = settings.SEARCH_TERM
        self.min_price = settings.MIN_PRICE
        self.max_price = settings.MAX_PRICE
        self.currency = settings.CURRENCY

        price_filter_url = '&rh=p_36%3A'  + str(self.min_price*100) + str(-self.max_price*100)
        search_term_url = 's?k=' + self.search_term
        self.clean_url = self.base_url + search_term_url + price_filter_url

        #The main browser
        print('Connecting to browser. This may take a while.')
        self.ff = Firefox()
        self.ff.set_browser_options(headless = False, incognito = True)
        self.ff.set_download_profile(animate_notifications = False)
        self.ff.set_browser()
        self.ff.search(self.clean_url)
        print('Done!!')

    def run(self):
        '''Run the AmazonAPI class.'''
        links = self.get_products_links()
        assert len(links)!=0, 'Not links found'        
        print('{} link(s) found'.format(len(links)))
        if not links:
            print('No links found')
            return None
        products = self.get_products_info(links)
        time.sleep(10)
        self.ff.disconnect()
        return products

    def get_products_links(self):
        '''
        Scrape the links of the products that are related to the item
            we are searching for.
        '''
        result_list = self.ff.browser.find_elements_by_class_name('s-result-list')
        links=[]
        try:
            results = result_list[0].find_elements_by_xpath(
                "//div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a")
            links = [link.get_attribute('href') for link in results]
            return links

        except Exception as error:
            print('Unable to find items')
            print(error)
            return links


    #Functions to get the info---------------------------------------------------------------------------------------------
    
    def get_products_info(self, links):
        '''Get the relevant information for each product on the list of links.'''
        asins = self.get_asins(links)
        products=[]
        for asin in asins:
            product = self.get_product_info(asin)
            products.append(product)
        return products

    def get_product_info(self, asin):    
        '''Get the relevant information of a SINGLE product.'''
        print('Product ID: {}  ||  Gathering data...'.format(asin))
        product_short_url = self.shorten_url(asin)
        self.ff.search('{}?language=en_US'.format(product_short_url))
        time.sleep(2)
        title = self.get_title()
        seller = self.get_seller()
        price = self.get_price()
        return {'asin' : asin,
            'url' : product_short_url,
            'title' : title,
            'seller' : seller,
            'price' : price}


    def get_asins(self, links):
        '''
        ASIN is the Amazon identification number. This is the way amazon tracks products.
        This function is going to return a list with the asins of each product in a given list of links.
        '''
        return [self.get_asin(link) for link in links]

    @staticmethod
    def get_asin(link):
        '''Get the asin of a SINGLE product.'''
        return link[link.find('/dp/')+4 : link.find('/ref')]
    
    def shorten_url(self, asin):
        '''Get the proper url for a product with a given asin.'''
        return self.base_url + '/dp/' + asin

    def get_title(self):
        '''Get the title of a product, while you are in the product page.'''
        try:
            return self.ff.browser.find_element_by_id('productTitle').text

        except Exception as error:
            print(error)
            print('Unable to find the name of the product')
            return self.search_term + '_undefined_name'


    def get_seller(self):
        '''Get the seller of a product, while you are in the product page.'''
        try:
            return self.ff.browser.find_element_by_id('bylineInfo').text

        except Exception as error:
            print(error)
            print('Unable to find the name of the product')
            return 'undefined_seller'


    def get_price(self):
        '''Get the seller of a product, while you are in the product page.'''
        price = None
        try:
            price = self.ff.browser.find_element_by_id('priceblock_ourprice').text
            price = self.convert_price(price)
        except NoSuchElementException:
            try:
                availability = self.ff.browser.find_element_by_id('availability').text
                if 'Available' in availability:
                    price = self.ff.browser.find_element_by_class_name('olp-padding-right').text
                    price = price[price.find(self.currency) :]
                    price =self.convert_price(price)
            except Exception as error:
                print(error)
                return 'Undefined-price'
        except Exception as error:
            print(error)
            return None
        return price


    def convert_price(self, price):
        '''Convert the price for the user.'''
        price = price.split(self.currency)[1]
        try:
            price = price.split("\n")[0] + "." + price.split("\n")[1]
        except:
            Exception()
        try:
            price = price.split(",")[0] + price.split(",")[1]
        except:
            Exception()
        return float(price)