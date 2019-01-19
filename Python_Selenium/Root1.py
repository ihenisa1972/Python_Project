from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
opts = Options()


opts = Options()
#opts.set_headless()
browser = Firefox(options=opts)
search_form = browser.get('https://bandcamp.com/login')
search_form = browser.find_element_by_id('username-field')
search_form.send_keys('ihenisa')
search_form = browser.find_element_by_id('password-field')
search_form.send_keys('Jehovah1914')
search_form.submit()




