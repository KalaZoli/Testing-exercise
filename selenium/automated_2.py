# Acceptance test #2 
# Acceptance criteria: You can change the langugae to portuguese
# With this test you can check if the language change is working properly

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class LiferayForms(unittest.TestCase):

    def setUp(self):
        #Open up the browser
        self.driver = webdriver.Chrome()

    def test_acceptance(self):
        driver = self.driver
        #Getting the URL for the form
        driver.get("https://forms.liferay.com/web/forms/shared/-/form/122548")
        language = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/form/div[1]/div/div/div/button").click()
        portuguese = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/ul/li/a").click()
        time.sleep(2)
        #Checking for the language change
        assert "Este é um Liferay Forms" in driver.title
        
        
        
    
    def tearDown(self):
        #Closing the browser after the test run
        self.driver.close()




if __name__ == "__main__":
    unittest.main()