from dotenv import load_dotenv, dotenv_values

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time

def webapp():

    URL = 'https://www.pythonanywhere.com/login/'

    config = dotenv_values(".env")

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('disable-notifications')
    options.add_argument('--disable-infobars')
    self.options.add_argument('--headless')

    driver = webdriver.Chrome('.chromedriver.exe', options = options)

    driver.get(URL)

    driver.find_element_by_name('auth-username').send_keys(config['email'])
    time.sleep(0.5)
    driver.find_element_by_name('auth-password').send_keys(config['pass'])

    driver.find_element_by_id('id_next').click()

    time.sleep(1)

    driver.get('https://www.pythonanywhere.com/user/abrohit/webapps/')
    time.sleep(0.5)
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[6]/div/div/div/form/input[2]").click()
    
if __name__ == '__main__':
    webapp()
