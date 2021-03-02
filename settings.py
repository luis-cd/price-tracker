#!/usr/bin/env
#-*- coding: utf-8 -*-
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

class Settings:

    def __init__(self):
        '''This are the settings for the scraper.'''
        self.DIRECTORY = 'reports'
        self.BASE_URL = 'https://www.amazon.com/'
        self.SEARCH_TERM = 'monitor 27"'
        self.MIN_PRICE = 20
        self.MAX_PRICE = 200
        self.CURRENCY = '$'



