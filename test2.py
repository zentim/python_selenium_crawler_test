from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


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
    driver.get("https://taqm.epa.gov.tw/taqm/tw/MonthlyAverage.aspx")

    driver.find_element(By.XPATH, '//*[@id="ctl05_btnQuery"]').click()
    time.sleep(1)

    titles = driver.find_elements(
        By.XPATH, '//*[@id="ctl05_gv"]/tbody/tr[1]/th')
    for title in titles:
        print(title.text)

    time.sleep(1)
    driver.close()
    driver.quit()


run()
