# code given

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
store = driver.find_elements_by_xpath('//*[@id="store"]')

for n in range(len(store) - 1, 0, -1):
    print(store[n].text())
can anyone explain the for loop ?
# it's scraping off a div on a website


# selenium skeleton

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()


# =====code breakdown======

# n (also commonly written as i) is the loop variable
# range(A, B, C)
# A is the starting number of the Loop (default 0)
# B is the ending number of the loop (required)
# C is the increment of the loop (default 1)
# for i in range(5): print(i)  =>   0, 1, 2, 3, 4
# for i in range(2, 5): print(i)  =>  2, 3, 4
# for i in range(5, 50, 5)  =>  5, 10, 15, 20, 25, 30, 35, 40, 45

# len() is a function that returns the number of items in an object

# summary:
# FOR variable n, loop this code.
# START the loop at the number of objects in the store variable - 1,
# END the loop at number 0
# Increment this loop by -1 each loop.
for n in range(len(store) -1, 0, -1):
    # the loop will run from a positive number (the number of objects in store minus one) until it hits 0
    # if the starting number is negative the loop will never end because it increments by -1, and the end condition is 0


# you should know what print() does

# variable[x] is a way to express the data inside of a list, table, dictionary, array, set, tuple etc.
# list = ["boomer", "zoomer", "doomer"]
# print(list[0])  =>  boomer
# array counts up from 0, 1, 2, etc
# you can also assign variables this way.
# list[0] = "consoomer"
# print(list[0])  =>  consoomer
# you can't assign variables to values not in the array AFAIK.
# list[3] = "bloomer"
# print(list[3])  =>  IndexError: list assignment index out of range

# I have no idea what .text does :linusweird:

#summary: print the value of store[number in array] with .text method
    print(store[n].text())
