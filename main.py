import os
import random
import sys

from selenium import webdriver

from Filename_creating import name_your_file


scrensot_name = name_your_file()+'.png'
my_bro = webdriver.Chrome()
my_bro.get('https://google.com/')
my_bro.save_screenshot('.\\screen\\' + scrensot_name)
my_bro.quit()

#todo: tidy up the code
#todo: put screenshotting into class
#todo: add create scrnsht folder + check
#todo: webdriver checker/downloader. how to check current chrome version 
#todo visual mode / report mode
#todo higthlight using page area 


print(name_your_file())

print('*****')
