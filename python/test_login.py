from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pytest
import logging

# def test_valid_login():
#     options = webdriver.ChromeOptions()
#     options.add_argument('--headless')
#     driver = webdriver.Chrome(options)
#     driver.get('https://www.saucedemo.com/')
#     driver.find_element(By.ID, 'user-name').send_keys('standard_user')
#     driver.find_element(By.ID, 'password').send_keys('secret_sauce')
#     driver.find_element(By.ID, 'login-button').click()


def test_logging():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    logger.debug("This is a debug message")
    assert True


@pytest.fixture
def sample_data():
    return [1, 2, 3]


def test_sum(sample_data):
    assert sum(sample_data) == 7


def test_sub(sample_data):
    assert sum(sample_data) == 7


@pytest.mark.parametrize("a, b, result", [(1, 2, 3), (4, 5, 9), (10, 20, 30)])
def test_addition(a, b, result):
    print('test', a, b, result)
    assert a + b == result


@pytest.mark.skip(reason="Skipping this test")
def test_not_needed():
    assert False


@pytest.mark.skipif(condition=False, reason="This test is skipped based on condition")
def test_conditionally_skipped():
    assert True
# class A():

#     def __init__(self):
#         self.greet = 'hello'

#     def greetings(self):
#         print(self.greet)


# class B(A):

#     def __init__(self):
#         self.greet = 'bye'

#     def greetings(self):
#         print(self.greet)


# class C(B, A):

#     def __init__(self):
#         self.greet = 'bye'
#         super().__init__()

#     def greetings(self):
#         print(self.greet)

#     # def greetings(self, value):
#     #     print(self.greet)


# a = A()
# a.greetings()


# def dec(func):
#     def wrapper(num1, num2):
#         print(num1, num2)
#         return func
#     return wrapper


# @dec
# def test(num1, num2):
#     pass


# test(1, 3)

