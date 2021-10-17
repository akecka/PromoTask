from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import load_chrome_browser
import login_data


class LoginPage:

    def __init__(self):
        self.driver = load_chrome_browser.ChromeDriver().get_driver()

    def page_login_logic(self, username, password):
        self.driver.get(login_data.url)
        self.driver.find_element(By.ID, login_data.login_form_id).send_keys(username)
        self.driver.find_element(By.ID, login_data.password_form_id).send_keys(password)
        self.driver.find_element(By.XPATH, login_data.button_form).click()

    def close_driver(self):
        self.driver.close()

    def check_logout_button_exists(self):
        delay = 10  # seconds
        try:
            WebDriverWait(self.driver, delay) \
                .until(expected_conditions.presence_of_element_located((By.CLASS_NAME, login_data.button_logout)))
            return True
        except TimeoutException:
            return False
