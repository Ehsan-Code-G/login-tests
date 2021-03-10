from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common_params import CommonParams
from locators import CommonLocators
import unittest
import os



class GmailLoginTestCase(unittest.TestCase):


    #Sets up the prerequisites of running tests
    def setUp(self):

        dirname = os.path.dirname(__file__)
        chrome_driver_path=dirname+"/chromedriver.exe"
        self.browser = webdriver.Chrome(chrome_driver_path)
        self.addCleanup(self.browser.quit)

    #Unsuccessful login with wrong password
    def test_unsuccessful_login(self):
        
        self.browser.get(CommonParams.Base_Url)
        WebDriverWait(self.browser, 15).until(EC.visibility_of_element_located(CommonLocators.User_Name_Box)).send_keys(CommonParams.Email_Address)
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(CommonLocators.Next_Button)).click()
        WebDriverWait(self.browser, 15).until(EC.visibility_of_element_located(CommonLocators.Password_Box)).send_keys("to"+CommonParams.Password+"ruin!")
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(CommonLocators.Submit_Button)).click()
        wrong_pass_msg = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(CommonLocators.Wrong_Msg_Tag)).get_attribute('innerText')
        self.assertIn("Wrong password",wrong_pass_msg)
        

    #Successful login to the gmail
    def test_successful_login(self):
        
        self.browser.get(CommonParams.Base_Url)
        WebDriverWait(self.browser, 15).until(EC.visibility_of_element_located(CommonLocators.User_Name_Box)).send_keys(CommonParams.Email_Address)
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(CommonLocators.Next_Button)).click()
        WebDriverWait(self.browser, 15).until(EC.visibility_of_element_located(CommonLocators.Password_Box)).send_keys(CommonParams.Password)
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(CommonLocators.Submit_Button)).click()
        self.browser.get("https://mail.google.com/")
        WebDriverWait(self.browser, 20).until(EC.title_contains("Inbox"))
        self.assertIn("Inbox",self.browser.title)        





if __name__ == '__main__':
    unittest.main()
