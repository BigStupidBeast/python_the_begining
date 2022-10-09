import random
from selenium import webdriver

my_bro = webdriver.Chrome()
my_bro.get('https://google.com/')

def add(*some_shift):
    """
    Function to explore asterix behavior
    :param some_shift:
    :return:
    """
    print(some_shift)


add(3, 'sd', 3, 5)

print(2**16)