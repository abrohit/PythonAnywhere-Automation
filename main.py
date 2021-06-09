from dotenv import dotenv_values

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time

class Automate():

    #Initializes class, Params: email and password of user.
    def __init__(self, email: str, password: str):

        self.BASEURL = ''


        self.options = Options()
        self.options.add_argument("--start-maximized")#Maximizes the browser.
        self.options.add_argument('disable-notifications')#Disables all notifcations.
        self.options.add_argument('--disable-infobars')#Removes 'Controlled by bot' on Chrome.
        self.options.add_argument('--headless')#Hides the browser.

        self.driver = webdriver.Chrome('chromedriver.exe', options = self.options)#Path to driver + Initializes driver.

        self.EMAIL = email
        self.PASS = password

    #Logs the user in.
    def login(self):

        self.driver.get('https://www.pythonanywhere.com/login/')#Gets login page.

        self.driver.find_element_by_name('auth-username').send_keys(self.EMAIL)#Enters Email.
        time.sleep(0.5)
        self.driver.find_element_by_name('auth-password').send_keys(self.PASS)#Enters Password.

        self.driver.find_element_by_id('id_next').click()#Clicks on login button.

        time.sleep(1)

        self.BASEURL = self.driver.current_url#Gets URL once logged in.
        
    #Runs Webapp forever.
    def webapp(self):

        self.driver.get(self.BASEURL + 'webapps/')#Once logged in driver loads webapp page.
        time.sleep(0.5)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[6]/div/div/div/form/input[2]").click()#Clicks on 'Run for 3 months' button.

    #Runs the task forever.
    def tasks(self):

        self.driver.get(self.BASEURL + 'tasks_tab/')#Once logged in driver loads tasks page.
        time.sleep(0.5)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[3]/div/div/table/tbody/tr/td[5]/button[4]").click()#Clicks on 'Extend Expiry' button.

    #Runs the functions.
    def run(self):

        self.login()
        self.webapp()
        self.tasks()

    #Quits the driver.
    def quit(self):
        self.driver.quit()
    
if __name__ == '__main__':

    config = dotenv_values(".env")
    
    webapp = Automate(config['email'], config['pass'])
    webapp.run()
    webapp.quit()
    
