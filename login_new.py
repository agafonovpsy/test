import unittest
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

class login_automationpractice(unittest.TestCase):

    def setUp (self):
        self.browser = webdriver.Chrome()
    
    def test_login_ap (self):
        browser = self.browser
        browser.get("http://automationpractice.com/index.php")
        self.assertIn("My Store", browser.title)
        browser.find_element_by_class_name("login").click()
        browser.implicitly_wait(10)
        browser.find_element_by_id("email").send_keys("seleniumisgood@mail.com")
        browser.find_element_by_id("passwd").send_keys("123456")
        browser.find_element_by_id("SubmitLogin").click()
        assert "My account - My Store" in browser.title
    
    def tearDown(self):
        self.browser.close()
    
if __name__ == "__main__":
    unittest.main()