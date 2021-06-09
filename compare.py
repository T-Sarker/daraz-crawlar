from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time
import pyttsx3

class ComparePrice:

    details2 =dict()
    def __init__(self):
        # declaring the driver
        # driver = webdriver.Chrome()
        self.engine = pyttsx3.init()
        product_name = input("Enter Product Name: ")
        self.startComparison(product_name)

    def say(self,text):
        # engine = pyttsx3.init()
        self.engine.say(text)
        self.engine.runAndWait()

    def startComparison(self,product_name):
        # declaring the driver
        driver = webdriver.Chrome()
        driver.maximize_window()

        # for x in range(0,3):
        driver.get("https://www.daraz.com.bd/")
        self.say("Waiting For data to load")
        time.sleep(5)
        searchBar = driver.find_element(By.ID,'q').send_keys(product_name)
        search_submit = driver.find_element(By.CLASS_NAME,'search-box__button--1oH7').submit()
        WebDriverWait(driver,5)
        time.sleep(3)
        # filter =driver.find_element(By.CLASS_NAME,'ant-select-selection--single').click()
        # self.say("Waiting For data")
        # time.sleep(3)
        # WebDriverWait(driver,15)
        # select_filter = driver.find_element(By.XPATH,'/html/body/div[6]/div/div/div/ul/li[2]').click()
        # WebDriverWait(driver, 15)
        # print("Filter Selected")
        # self.say("Filter Selected")
        # self.say("Now Waiting For data")
        time.sleep(5)
        try:
            # getting the products
            all_products = driver.find_element(By.CLASS_NAME,'c1_t2i')
            products = all_products.find_element(By.CLASS_NAME,'c2prKC')

            print("sleeping")
            self.say("Loading the data")
            time.sleep(5)

            title = products.find_element(By.CLASS_NAME, 'c16H9d').find_element(By.TAG_NAME, 'a').text
            price = products.find_element(By.CLASS_NAME, 'c3gUW0').find_element(By.TAG_NAME, 'span').text
            review = products.find_element(By.CLASS_NAME,'c3XbGJ').text
            link = products.find_element(By.CLASS_NAME, 'c16H9d').find_element(By.TAG_NAME, 'a').get_attribute('href')

            # storing the details into a dictonary
            self.details2['title'] = title,
            self.details2['price'] = price,
            self.details2['review'] = review,
            self.details2['link'] = link


            # if want to get all the poduct of the page
            # for pro in products:
            #     # print(*pro)
            #     title = pro.find_element(By.CLASS_NAME, 'c16H9d').find_element(By.TAG_NAME, 'a').text
            #     price = pro.find_element(By.CLASS_NAME, 'c3gUW0').find_element(By.TAG_NAME, 'span').text
            #
            #     # storing the details into a dictonary
            #     self.details2[title] = price
            #     # print(title + "-->" + price.strip('৳ '))
            #
            #     print(self.details)
            #     print("+++++++++++++++++++++++++++++++++++++++++++++++++")
            #     print(self.details2)
        except Exception:
            print("problem Found"+NoSuchElementException)

        print(self.details2)





obj = ComparePrice()