# Acceptance test #1 
#You can change the langugae to portuguese
#
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class LiferayForms(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_acceptance(self):
        driver = self.driver
        driver.get("https://forms.liferay.com/web/forms/shared/-/form/122548")
        language = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/form/div[1]/div/div/div/button").click()
        portuguese = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/ul/li/a").click()
        # name = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/form/div[3]/div/div/div/div[1]/div/div/div[1]/div[1]/div/input")
        # name.send_keys("John Smith")
        # calender = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/form/div[3]/div/div/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div/button").click()
        # birthdate = driver.find_element_by_xpath("//div[contains(text(),'10')]").click()
        # text = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/form/div[3]/div/div/div/div[1]/div/div/div[2]/div/div/textarea")
        # text.send_keys("some random text")
        # submit = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/form/div[3]/div/div/div/div[2]/button").click()
        time.sleep(10)
        
        
    
    def tearDown(self):
        self.driver.close()




if __name__ == "__main__":
    unittest.main()