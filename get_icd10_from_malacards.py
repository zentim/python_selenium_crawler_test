from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from datetime import timedelta
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

def get_malacards_obj(driver, url):
    driver.get(url)

    # target structure
    malacards_obj = {
        'MCID': '',
        'name': '',
        'source_url': '',
        'ICD10': [],
        'sign_or_symptoms': [],
        'HOP_symptoms': []
    }

    # get url
    malacards_obj['source_url'] = url
    driver.get(url)
    time.sleep(1)

    # find MCID of malacards
    MCID = driver.find_element(By.XPATH, '//*[@id="top-card"]/div[1]/table/tbody/tr[1]/td[1]/div/div/div/div[1]').text.split(None, 1)[1]
    malacards_obj['MCID'] = MCID

    # find disease name
    disease_name = driver.find_element(By.XPATH, '//*[@id="top-card"]/div[1]/table/tbody/tr[1]/td[2]/div/h1/span').text
    malacards_obj['name'] = disease_name

    # find ICD10
    try:
        # ICD10_title = driver.find_element(By.XPATH, '//b[@title="International Classification of Diseases, 10th Revision"]').text
        ICD10s = driver.find_elements(By.XPATH, '//div[contains(@id, "ExternalId_item")]/a[contains(@href, "http://apps.who.int/classifications/icd10/browse/2016/en#/")]')
        icd_arr = []
        for icd in ICD10s:
            if icd.text != '34' or icd.text != '35':
                icd_arr.append(icd.text)
        malacards_obj['ICD10'] = icd_arr
    except NoSuchElementException:
        print('!!! ICD10 not found !!!')

    # find sign or symptoms
    try:
        sign_or_symptoms = driver.find_elements(By.XPATH, '//span[contains(@itemprop, "signOrSymptom")]/span[contains(@itemprop, "name")]/span')
        sos_arr = []
        for sos in sign_or_symptoms:
            sos_text = sos.text
            if (sos.text[-1:] == ','):
                sos_text = sos.text[:-1]
            sos_arr.append(sos_text)
        malacards_obj['sign_or_symptoms'] = sos_arr
    except NoSuchElementException:
        print('!!! Symptoms not found !!!')

    # find HPO_Symptoms-table_SeeMore
    try:
        see_more_btn = driver.find_element(By.XPATH, '//a[@id="HPO_Symptoms-table_SeeMore"]')
        see_more_js = see_more_btn.get_attribute('href').replace("javascript:", "")

        driver.execute_script(see_more_js)
    except NoSuchElementException:
        print('!!! HPO_Symptoms-table_SeeMore not found !!!')

    # find HPO_Symptoms
    try:
        HOP_symptoms = driver.find_elements(By.XPATH, '//table[@id="HPO_Symptoms-table"]/tbody/tr/td[2]')
        sos_arr = []
        for sos in HOP_symptoms:
            sos_text = sos.text
            while sos_text.split(None)[-1] == '33' or sos_text.split(None)[-1] == '60':
                sos_text = sos_text[:-3]
            sos_arr.append(sos_text)
        malacards_obj['HOP_symptoms'] = sos_arr
    except NoSuchElementException:
        print('!!! HPO_Symptoms not found !!!')

    return malacards_obj



def run():
    folder = 'malacards_bone_diseases_category'
    if not os.path.exists(folder):
        os.makedirs(folder)

    driver = get_driver()

    # get url
    url = 'https://www.malacards.org/categories/bone_disease_list'
    driver.get(url)
    time.sleep(1)

    # collect malacards urls from the url
    print('\nStart collect malacards urls...\n')
    urls = []
    malacards_rows = driver.find_elements(By.XPATH, '//td[4]/a')
    for row in malacards_rows:
        urls.append(row.get_attribute('href'))
        print(str(len(urls)) + ': ' + row.get_attribute('href'))

    # for test
    # urls = ['https://www.malacards.org/card/osteopetrosis_autosomal_recessive_3_2?search=Bone%20diseases#clinical_features']

    # collect malacards objs
    print('\nStart collect malacards objs...\n')

    start_time = time.monotonic()

    # main
    malacards_arr = []
    start_index = 1500
    num = start_index
    split_num = 100
    for url in urls[start_index:]:
        # get each disease's malacards_obj by url
        obj = get_malacards_obj(driver, url)
        malacards_arr.append(obj)
        num = num + 1
        print(str(num) + ': ' + obj['name'])

        if (num % split_num == 0):
            # output json result
            filename = "malacards_bone_diseases_category_" + str(num - split_num + 1) + "_" + str(num) + ".json"
            fo = open(folder + '/' + filename, "w")
            encodedjson = json.dumps(malacards_arr)
            print('Output: ' + filename)
            fo.write(encodedjson)
            fo.close()
            malacards_arr = []

    end_time = time.monotonic()
    print("\n--- Spend %s to collect malacards objs. ---\n" % timedelta(seconds=end_time - start_time))

    # output json for the rest result
    if len(malacards_arr) > 0:
        filename = "malacards_bone_diseases_category_" + str(num - split_num + 1) + "_" + str(num) + ".json"
        fo = open(folder + '/' + filename, "w")
        encodedjson = json.dumps(malacards_arr)
        print('Output: ' + filename)
        fo.write(encodedjson)
        fo.close()

    
    print('finish!')
    time.sleep(1)
    driver.close()
    driver.quit()


run()
