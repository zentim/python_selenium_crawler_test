from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os
import json


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
    driver = get_driver()
    driver.get("https://icd.who.int/browse10/2016/en")
    time.sleep(3)

    # open menu
    for num in range(2, 235):
        target = '//*[@id="ygtvt' + str(num) + '"]/a'
        try:
            driver.find_element(By.XPATH, target).click()
            print(str(num) + ' clicked')
            time.sleep(1)
        except NoSuchElementException:
            print('======== Target:' + target + ' not exist! ==========')
            break
    
    # get text elements
    elems = driver.find_elements(By.XPATH, '//a[@class="ygtvlabel  "]')

    
   

    # collect text
    icd10_text = ''
    icd10_dict = []

    for e in elems:
        # print(e.text)
        s = e.text
        obj = {'code': s.split(None, 1)[0], 'name': s.split(None, 1)[1]}
        icd10_text += (s + '\n')
        icd10_dict.append(obj)
        
    # output result
    fo = open("icd10_XXX.txt", "w")
    fo.write(icd10_text)
    fo.close()


    # output json result
    fo = open("icd10_XXX.json", "w")
    encodedjson = json.dumps(icd10_dict)
    fo.write(encodedjson)
    fo.close()

    print('finish!')
    time.sleep(1)
    driver.close()
    driver.quit()


run()
