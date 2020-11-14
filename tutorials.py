from selenium import webdriver
import time
import requests, time, random
from bs4 import BeautifulSoup
import pandas
import csv
import io
import urllib
import codecs



# specifies the path to the chromedriver.exe
driver = webdriver.Chrome(r"C:\Users\tomar\Downloads\chromedriver.exe")

#driver.get method() will navigate to a page given by the URL address
url = r"http://demo.automationtesting.in/Windows.html"

#webdriver 
driver.get(url)
time.sleep(1)
print(driver.current_url)   
driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()
time.sleep(1)
print(driver.current_url)
driver.quit()

#forword backword
driver.get(url)
time.sleep(1)
print(driver.title)
driver.get(url1)
time.sleep(1)
driver.back()
time.sleep(1)
print(driver.title)
driver.forward()
time.sleep(1)
print(driver.title)
driver.quit()

# is enable or disabled
driver.find_elements_by_class_name(username)
driver.is_displayed()
driver.is_enabled()

driver.find_element_by_css_selector("input[value=hello]")
driver.is_selected()

#maximize windows
driver.maximize_window()

#explicite wait
driver.implicitly_wait(5)
from selenium.webdriver.support.ui import WebDriverWait
# loadin a apge and wait maximize 10s
wait = WebDriverWait(driver, 10) #maximum 10s wait 
# element select and continue 
element = wait.until(EC.element_to_be_clickbale((By.id, "id")))


# radio button select then .click()

# dropdown select 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
element = driver.find_element_by_css_selector()
drp = Select(element)
drp.select_by_index(1)
drp.select_by_value("")
drp.select_by_visible_text("")
all_options = drp.options() #get all options


#work with link

driver.switch_to_alert().dismiss()

driver.find_element(By.PARTIAL_LINK_TEXT, "reg")

# ifram
driver.switch_to.frame("name of fram")
driver.find_element_by_link_text("click here").click()

# go back to the main page then you can access other frame
driver.switch_to.default_content()

driver.switch_to.frame("name of other fram")
driver.find_element_by_link_text("cleck here")
driver.switch_to.default_content()

# browser windows handle
print(driver.current_window_handle)
print(driver.window_handles)
handles = driver.window_handles #return all windows value
for valu in handles:
    driver.switch_to.window(valu)
    time.sleep(5)
    print(driver.title)
    
    driver.close()

# mouse actions movement
frist = driver.find_element_by_xpath("xpath")
second = driver.find_element_by_xpath("xpath")
third = driver.find_element_by_xpath("xpath")

from selenium.webdriver import ActionChains
actions = ActionChains(driver)
actions.move_to_element(frist).move_to_element(second).move_to_element(third).click().perform()
actions.double_click(frist).perform() #double click
actions.context_click(frist).perform() #write click
actions.drag_and_drop(frist, second).perform() #deag and drop

# chrome option settings 
from selenium.webdriver.chrome.options import Options
options = Options.add_encoded_extension('prefs', {"download.default_directory": "c\path"})

driver = webdriver.Chrome(executable_path=url, chrome_options=options)

#screen short
driver.get_screenshot_as_file("screenshot.png") #only take png
driver.save_screenshot("path") #any kind of extention .jpg .png

#log file save 
import logging
logging.basicConfig(filename="path .log",
format='%(asctime)s: %(levelname)s: %(message)s'
 level=logging.DEBUG)
logging.debug("this is debug")
logging.error("error")
logging.warning("wornign")
logging.info("info")
logging.critical('critical')

# unitTest


import unittest


def setUpModule():
    print("this will execute before module start")
def tearDownModule():
    print("this will execute after module fininsh")

class Test(unittest.TestCase):
    @classmethod
    def setUp(self):
        print('this is start befor method start')
    @classmethod
    def tearDown(self):
        print("this is start after method finished")
    @classmethod
    def setUpClass(self):
        print('this start before class start')
    @classmethod
    def tearDownClass(self):
        print('this start after finish class')
    
    def test_firstcase(self):
        print("this is my first test case")
    
    def test_secound(self):
        print("this is my first test case")
    
    @unittest.SkipTest
    def skip_test(self):
        print("skip test case")
    @unittest.skip("this is not ready yet")
    def skip_only(self):
        print("skip with msg")
    @unittest.skipIf(1==1, "1==1 is not correct")
    def skip_with_condition(self):
        print("skip with condition")
    

    # assertion method
    def testName(self):
        driver = webdriver.Chrome(executable_path="path")
        driver.get(url)
        title = driver.title
        
        self.assertEqual("title", title, "error meg") #if title equal google
        self.assertNotEqual() #so many condition are there

    

if __name__ == "__main__":
    unittest.main()


# suppose we have more than one test package1, pageage2 
from package1.test1 import class1
from package2.test2 import class2

tc1 = unittest.TestLoader.loadTestsFromTestCase(class1)
tc2 = unittest.TestLoader.loadTestsFromTestCase(class2)

testSuite = unittest.TestSuite([tc1, tc2])
unittest.TextTestRunner().run(testSuite)
unittest.TextTestRunner(verbosity=2).run(testSuite)