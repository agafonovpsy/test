# import time
# import pytest


# @pytest.fixture(scope='class', autouse=True)
# def suite_data():
#     print("\n> Suite setup")
#     yield
#     print("> Suite teardown")

    
# @pytest.fixture(scope='function')
# def case_data():
#     print("   > Case setup")
#     yield time.time()
#     print("\n   > Case teardown")

import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="./chromedriver")
    yield driver
    driver.quit()