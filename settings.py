#!/usr/bin/env
#-*- coding: utf-8 -*-
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

class Settings:
    '''This are the settings for the price tracker.'''
    def __init__(self):
        self.DIRECTORY = 'reports'
        self.SEARCH_TERM = 'camiseta Red Hot Chili Peppers'
        self.FILTERS = {'min': MIN_PRICE,
        'max': MAX_PRICE}
        self.MIN_PRICE = '5'
        self.MAX_PRICE = '250'
        self.BASE_URL = 'https://www.amazon.es/'
        self.CURRENCY = '€'

 
    


#https://www.youtube.com/watch?v=WbJeL_Av2-Q