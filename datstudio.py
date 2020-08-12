#Load nessary libray and set driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
PATH = '/Users/nfishel/chromedriver'
driver = webdriver.Chrome(PATH)



#login to google
def login(): 
    driver.get('https://accounts.google.com/o/oauth2/auth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3ABBC%2C16%3A7871a518454d9858%2C10%3A1596044743%2C16%3Ac3acd63543d97f0e%2C8ec8db2da19b6e3a12611aeba769828bbf4e1ecfc4fc09635849a4d5fde7beb0%22%2C%22cdl%22%3Anull%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%221adeaf729bad482f870d31ffc062b90a%22%7D&response_type=code&flowName=GeneralOAuthFlow')
    url = driver.current_url
    correct = False
    while correct == False:
        if 'https://stackoverflow.com/' in url:
            correct = True
            data_studio()
        else:
            url = driver.current_url
            print(url)
    
#helper fuction for the login
#go to datastudio after the user logs in
def data_studio():
    driver.get('https://datastudio.google.com')


#create report in datastudio
def create_report():
    driver.implicitly_wait(5)
    btn = driver.find_element_by_class_name("gmat-fab-label-container")
    btn.click()
    driver.implicitly_wait(1)
    btn = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/button[1]')
    btn.click()




login()
create_report()


