#!/usr/bin/env
#-*- coding: utf-8 -*-
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

class Settings:

    def __init__(self):
        '''This are the settings for the price tracker.'''
        self.DIRECTORY = 'reports'
        self.SEARCH_TERM = 'ps4'
        self.MIN_PRICE = '275'
        self.MAX_PRICE = '600'
        self.FILTERS = {'min' : self.MIN_PRICE,
            'max' : self.MAX_PRICE}
        self.BASE_URL = 'https://www.amazon.es/'
        self.CURRENCY = '€'