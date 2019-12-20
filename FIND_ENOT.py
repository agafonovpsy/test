#Задание: найти ЕНОТА в вкипедии
import pytest

from selenium import webdriver

link = "http://www.yandex.ru/"

def link_t(link):
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_id("input__control input__input").send_keys("Енот википедия")
    browser.find_element_by_type("submit").click()

if __name__ == "__main__":
    pytest.main()