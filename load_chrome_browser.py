from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class ChromeDriver:

    def get_driver(self):
        options = Options()
        options.page_load_strategy = 'normal'
        return webdriver.Chrome("C:\\Selenium-drivers\\Chrome\\chromedriver.exe", options=options)
