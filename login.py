import pytest

from selenium import webdriver

link = "http://automationpractice.com/index.php"

browser = webdriver.Chrome()
browser.get(link)
browser.find_element_by_class_name("login").click()
browser.implicitly_wait(10)
browser.find_element_by_id("email").send_keys("seleniumisgood@mail.com")
browser.find_element_by_id("passwd").send_keys("123456")
browser.find_element_by_id("SubmitLogin").click()
assert "My account - My Store" in browser.title
browser.close()