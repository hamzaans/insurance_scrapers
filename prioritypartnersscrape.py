from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

j = 0
while j < 10:
    driver = webdriver.Chrome()
    URL = "https://pp.healthtrioconnect.com/public-app/consumer/provdir/search.page?distance=25&startRow={page}0&sortType=DISTANCE&provType=S&myZip=20602".format(page = j)
    driver.get(URL)
    time.sleep(3) 

    i = 1
    while i < 300:
             
        doctor_name = driver.find_element(By.XPATH, '/html/body/div[4]/div/form/div/div[1]/div[6]/table/tbody/tr[{row}]/td[1]/h3/a'.format(row = i))
        specialty = driver.find_element(By.XPATH, '/html/body/div[4]/div/form/div/div[1]/div[6]/table/tbody/tr[{row}]/td[1]/span[1]'.format(row = i))
        group = driver.find_element(By.XPATH, '/html/body/div[4]/div/form/div/div[1]/div[6]/table/tbody/tr[{row}]/td[3]/div'.format(row = i))
        address = driver.find_element(By.XPATH, '/html/body/div[4]/div/form/div/div[1]/div[6]/table/tbody/tr[{row}]/td[3]/address/span[1]'.format(row = i))
        phone = driver.find_element(By.XPATH, '/html/body/div[4]/div/form/div/div[1]/div[6]/table/tbody/tr[{row}]/td[3]/address/span[2]'.format(row = i))
        print(doctor_name.text)
        print(specialty.text)
        print(group.text)
        print(address.text)
        print(phone.text)
        print()
        i += 1
    j += 1
    driver.close()
    


            


