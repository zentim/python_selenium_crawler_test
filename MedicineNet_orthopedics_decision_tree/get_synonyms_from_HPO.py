from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from datetime import timedelta
import os
import json
import math


def get_driver():
    dirpath = os.getcwd()

    # Chrome auto install driver
    # from webdriver_manager.chrome import ChromeDriverManager
    # driver = webdriver.Chrome(ChromeDriverManager().install())

    # IE auto install driver
    # from webdriver_manager.microsoft import IEDriverManager
    # driver = webdriver.Ie(IEDriverManager().install())

    # Edge auto install driver
    # from webdriver_manager.microsoft import EdgeDriverManager
    # driver = webdriver.Edge(EdgeDriverManager().install())

    # Chrome
    driver = webdriver.Chrome(
        dirpath + '/driver/chrome_version_76/chromedriver.exe')

    # IE
    # driver = webdriver.Ie(
    #     dirpath + '/driver/IEDriverServer_x64_3.141.0/IEDriverServer.exe')

    # Edge
    # driver = webdriver.Edge(
    #     dirpath + '/driver/MicrosoftWebDriver/MicrosoftWebDriver.exe')
    return driver



def run():
    folder = 'dataset'
    if not os.path.exists(folder):
        os.makedirs(folder)

    driver = get_driver()

    # get url
    url = 'https://hpo.jax.org/app/browse/term/HP:0002829'
    driver.get(url)
    time.sleep(1)

    # read dataset
    medicine_net_symptom_list = []
    path = os.getcwd() + '/dataset/'
    filename = 'medicine_net_symptom_list.json'
    with open(path + filename, 'r') as reader:
        jf = json.loads(reader.read())
        for obj in jf:
            medicine_net_symptom_list.append(obj)
    
    # search HPO
    for obj in medicine_net_symptom_list:
        url = "https://hpo.jax.org/app/browse/search?q=" + obj + "&navFilter=all"
        driver.get(url)
        time.sleep(1)

        try:
            ele = driver.find_element(By.XPATH, '//*[@id="mat-tab-content-0-0"]/div/div[1]/div/mat-table/mat-row/mat-cell[1]/a')
            print(ele.text)
            time.sleep(1)
        except NoSuchElementException:
            print('!!! No such element !!!')
    

    
    print('finish!')
    time.sleep(1)
    driver.close()
    driver.quit()


run()
