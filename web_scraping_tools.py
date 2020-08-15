#!/usr/bin/env
#-*- coding: utf-8 -*-
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys

# from selenium.webdriver.chrome.options import Options #solo de usar chrome
# chrome_options = Options()
# #chrome_options.add_argument("--disable-extensions")
# #chrome_options.add_argument("--disable-gpu")
# #chrome_options.add_argument("--no-sandbox") # linux only
# chrome_options.add_argument("--headless") #correr chrome en version headless
#-------------------------------------------------------------------------------------------------------------------------------------------------------------


path_to_firefox='/usr/bin/firefox' #directorio del buscador
executable_path='/usr/local/bin/geckodriver' #directorio del driver del buscador

def set_profile(down_dir=1):
    '''Configura las opciones de descarga para evitar el diálogo. 
    down_dir=0, descarga en escritorio,
    con 1 descarga en Descargas, 
    con 2, descarga en un directorio que configuremos. 
    Ver:
    https://www.lifewire.com/firefox-about-config-entry-browser-445707
    '''
    profile=webdriver.FirefoxProfile()
    profile.set_preference('browser.download.folderList', down_dir) #configura directorio de descarga
    profile.set_preference('browser.download.manager.showWhenStarting', False)
    profile.set_preference('browser.download.dir', '/tmp')
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')
    return profile

#-------------------------------Conectar y desconectar a una página-------------------------------------------------------------------------------------------


def connect(web, title):
    '''Elegimos el navegador y entramos en la web de MeteoGalicia.
    input:
        web: str con el link de la página.
        title: str con una parte del título de la página, para comprobar.
    '''
    binary=FirefoxBinary('/usr/bin/firefox')
    page=webdriver.Firefox(firefox_binary=binary,
        executable_path='/usr/local/bin/geckodriver',
        firefox_profile=set_profile())
    page.get(web)
    assert title in page.title, 'Página incorrecta.'
    return page


def disconnect(page):
    '''Cierra todo al finalizar.
    Lo pongo como otra función para trabajar luego con excepciones aquí.
    '''
    page.quit()



#------------------------------Acciones del buscador---------------------------------------------------------------------------------------------

def click_checkbox(page, identificacion):
    '''Busca elemento por id, y pincha en él.
    También sirve para descargas con on click events con el profile correcto.
    '''
    button=page.find_element_by_id(identificacion)
    button.click()


def enter_text(page, identificacion, text):
    text_box=page.find_element_by_id(identificacion)
    page.send_keys(text)
    page.send_keys(Keys.ENTER)