from selenium import webdriver
import time
import os

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

driver.get("https://google.com")
time.sleep(2)
driver.close()
driver.quit()
