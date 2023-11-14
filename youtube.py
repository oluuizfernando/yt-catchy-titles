from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service()
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=options, service=service)

url = 'https://www.youtube.com/'

driver.get(url)

pesquisa = str(input('Pesquisar por > '))

#time.sleep(2)
#a = driver.find_element(By.XPATH, '//*[@id="search-form"]')
#a.click()

a = driver.find_element(By.NAME, 'search_query')
a.clear()
a.send_keys(pesquisa)
a = driver.find_element(By.XPATH, '//*[@id="search-icon-legacy"]/yt-icon/yt-icon-shape/icon-shape/div')
a.click()