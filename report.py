#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#---------------------------------------------------------------------------------------------------------------------
import json
from datetime import datetime
#---------------------------------------------------------------------------------------------------------------------


class GenerateReport:
    def __init__(self, settings, data):
        '''Create the report of the information.'''
        self.directory=settings.DIRECTORY
        self.data = data
        self.base_url = settings.BASE_URL
        self.search_term = settings.SEARCH_TERM
        self.filters = {'min' : settings.MIN_PRICE,
            'max' : settings.MAX_PRICE}
        self.currency = settings.CURRENCY

    def run_report(self):
        '''Start the report.'''
        print('Generating report...')        
        report = {
        'title' : self.search_term,
        'date' : self.get_now(),
        'best_item' : self.get_best_item(),
        'currency' : self.currency,
        'filters' : self.filters,
        'products' : self.data}
        print(report)
        file_name = self.directory + '/' + self.search_term + '_' + self.get_now() + '.json'
        with open(file_name, 'w') as file:
            json.dump(report, file)
        print('Done!!')

    @staticmethod
    def get_now():
        '''Get current date and hour.'''
        return datetime.now().strftime('%d-%m-%Y')

    def get_best_item(self):
        '''Find the best item of the ones found. (The chepest)'''
        try:
            return sorted(self.data, key=lambda k: k['price'])[0]
        except Exception as error:
            print(error)
            print('Unable to get the best price.')
            return None