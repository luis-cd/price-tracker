#!/usr/bin/env
#-*- coding: utf-8 -*-
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
import web_scraping_tools as wst

class AmazonAPI:
    def __init__(self,search_term,filters,base_url,currency):
        self.base_url=base_url
        self.search_term=search_term