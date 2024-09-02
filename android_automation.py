from appium import webdriver
import time

class AndroidAutomation:
    def __init__(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "Android Emulator",
            "appPackage": "com.facebook.katana",
            "appActivity": ".LoginActivity",
            "noReset": True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def login_facebook(self, username, password):
        email_field = self.driver.find_element_by_id("com.facebook.katana:id/login_username")
        email_field.send_keys(username)

        password_field = self.driver.find_element_by_id("com.facebook.katana:id/login_password")
        password_field.send_keys(password)

        login_button = self.driver.find_element_by_id("com.facebook.katana:id/login_login")
        login_button.click()
        time.sleep(5)

    def capture_screenshot(self, filename):
        self.driver.save_screenshot(filename)
        print(f"Screenshot saved as {filename}")

    def close(self):
        self.driver.quit()
