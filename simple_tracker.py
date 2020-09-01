#!/usr/bin/env
#-*- coding: utf-8 -*-
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
from settings import Settings
from amazon_api import AmazonAPI
from report import GenerateReport
#-----------------------------------------------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    
    settings=Settings()
    amazon=AmazonAPI(settings)
    amazon.run()
