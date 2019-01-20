from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
opts = Options()


opts = Options()
browser = Firefox(options=opts)
search_form = browser.get('https://espn.com')
search_form = browser.find_element_by_link_text('NBA')
search_form.click()
search_form = browser.find_element_by_link_text('Standings')
search_form.click()

'''search_form.send_keys('ihenisa')
search_form = browser.find_element_by_id('password-field')
search_form.send_keys('Jehovah1914')
search_form.submit()'''




