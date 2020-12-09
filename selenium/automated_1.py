# Acceptance test #1 
#  Acceptance criteria: You can submit the form after filling the form with valid data
# With this test you can test if the form is getting submitted properly

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
        name = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/form/div[3]/div/div/div/div[1]/div/div/div[1]/div[1]/div/input")
        name.send_keys("John Smith")
        name.send_keys(Keys.ENTER)
        calender = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/form/div[3]/div/div/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div/button").click()
        birthdate = driver.find_element_by_xpath("//div[contains(text(),'10')]").click()
        text = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/form/div[3]/div/div/div/div[1]/div/div/div[2]/div/div/textarea")
        text.send_keys("some random text")
        submit = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div/form/div[3]/div/div/div/div[2]/button").click()
        time.sleep(2)
        #Checking if the form is being submitted successfully
        assert "Form - Forms" in driver.title
        
        
    
    def tearDown(self):
        #Closing the browser after the test run
        self.driver.close()




if __name__ == "__main__":
    unittest.main()