#Задание: найти ЕНОТА в вкипедии
import pytest

from selenium import webdriver

link = "http://www.yandex.ru/"

browser = webdriver.Chrome()
browser.get(link)
browser.find_element_by_id("text").send_keys("Енот википедия\n")

if name == "main":
    pytest.main()