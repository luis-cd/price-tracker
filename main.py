#!/usr/bin/env
#-*- coding: utf-8 -*-
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
import web_scraping_tools as wst
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

web='https://www.amazon.es/'
title='Amazon.es'
page=wst.connect(web,title)

text_box_id='twotabsearchtextbox'
tracked_element='cocacola'

wst.enter_text(page,text_box_id, tracked_element)
