#!/usr/bin/env
#-*- coding: utf-8 -*-
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
from easelenium.firefox_selenium import Firefox

class AmazonAPI:
    def __init__(self,search_term,filters,base_url,currency):
        self.base_url=base_url
        self.search_term=search_term