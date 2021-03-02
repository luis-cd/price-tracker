#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
from settings import Settings
from amazon_api import AmazonAPI
from report import GenerateReport
#-----------------------------------------------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    
    settings = Settings()
    amazon = AmazonAPI(settings)
    data = amazon.run()
    GenerateReport(settings, data).run_report()