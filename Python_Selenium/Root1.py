from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


opts = Options()
browser = Firefox(options=opts)
search_form = browser.get('https://espn.com')
search_form = browser.find_element_by_link_text('NBA')
search_form.click()
search_form = browser.find_element_by_link_text('Standings')
search_form.click()






