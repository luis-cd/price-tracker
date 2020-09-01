#!/usr/bin/env
#-*- coding: utf-8 -*-
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
from easelenium.firefox_selenium import Firefox
import time
#-----------------------------------------------------------------------------------------------------------------------------------------------------------


class AmazonAPI:

    def __init__(self,settings):
        '''This class would do the work of scraping Amazon pages.''' 
        #The basic information.
        self.base_url = settings.BASE_URL
        self.search_term = settings.SEARCH_TERM
        self.filters = settings.FILTERS
        #price filter is like this to match the amazon URL system.
        self.price_filters = '&rh=p_36%3A{0}00-{1}00'.format(self.filters['min'],self.filters['max'])
        self.currency = settings.CURRENCY

    def run(self):
        '''Run the AmazonAPI class.'''
        self.ff = Firefox()
        self.ff.set_browser_options(headless = False, incognito = True)
        self.ff.set_download_profile(animate_notifications = False)
        self.ff.set_browser()
        self.ff.search(self.base_url)

        links = self.get_products_links()
        print('{} link(s) found'.format(len(links)))

        products = self.get_products_info(links)
        #time.sleep(10)
        #self.ff.disconnet()

    def get_products_links(self):
        '''
        Scrape the links of the products that are related to the item
            we are searching for.
        '''
        self.ff.enter_text_and_go(xpath='//*[@id="twotabsearchtextbox"]',
            text=self.search_term)

        time.sleep(2)
        self.ff.browser.get('{0}{1}'.format(self.ff.browser.current_url,
            self.price_filters))
        time.sleep(2)

        result_list = self.ff.browser.find_element_by_class_name('s-result-list')
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

