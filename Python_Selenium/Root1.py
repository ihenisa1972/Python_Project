from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from time import sleep, ctime
from collections import namedtuple
from threading import Thread
from os.path import isfile
import csv


'''
search_form = browser.get('https://espn.com')
search_form = browser.find_element_by_link_text('NBA')
search_form.click()
search_form = browser.find_element_by_link_text('Standings')
search_form.click()'''

class WebCrawler():
    def __init__(self):
        # Create a headless browser
        opts = Options()
        self.browser = Firefox(options=opts)

    def getbrowser(self, website):
        self.search_form = self.browser.get(website)

if __name__ == '__main__':
    website = WebCrawler()
    website.getbrowser('https://espn.com')








