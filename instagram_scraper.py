from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import time
from getpass import getpass
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InstagramScraper:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = None
        self.screenshot_dir = "assets/screenshots"
        os.makedirs(self.screenshot_dir, exist_ok=True)

    def login(self):
        options = Options()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("https://www.instagram.com/accounts/login/")
        try:
            username_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_input = self.driver.find_element(By.NAME, "password")
            username_input.send_keys(self.username)
            password_input.send_keys(self.password)
            password_input.submit()
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("https://www.instagram.com/")
            )
        except TimeoutException:
            logging.error("Login failed")
            self.close()
            exit(1)

    def get_user_profile_url(self, target_username=None):
        if target_username is None:
            target_username = self.username
        return f"https://www.instagram.com/{target_username}/"

    def scrape(self, target_username=None):
        url = self.get_user_profile_url(target_username)
        self.driver.get(url)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.url_contains(url)
            )
        except TimeoutException:
            logging.error("Failed to load user profile page")
            self.close()
            exit(1)

        # Take screenshots of all relevant sections
        sections = ['posts', 'followers', 'following', 'about']
        for section in sections:
            self.scrape_section(section)

    def scrape_section(self, section):
        scraping_functions = {
            'posts': self.scrape_posts,
            'followers': self.scrape_followers,
            'following': self.scrape_following,
            'about': self.scrape_about
        }

        if section in scraping_functions:
            scraping_functions[section]()
        else:
            logging.error(f"Invalid section: {section}")

    def scrape_posts(self):
        # Implement specific code to scroll through posts and capture screenshots
        logging.info("Scraping posts")
        # Add your code here

    def scrape_followers(self):
        # Implement specific code to scroll through followers and capture screenshots
        logging.info("Scraping followers")
        # Add your code here

    def scrape_following(self):
        # Implement specific code to scroll through following and capture screenshots
        logging.info("Scraping following")
        # Add your code here

    def scrape_about(self):
        # Implement specific code to capture about section
        logging.info("Scraping about section")
        # Add your code here

    def generate_report(self):
        report_file = "assets/reports/instagram_report.html"
        with open(report_file, "w") as file:
            file.write("<html><body>")
            file.write("<h1>Instagram Report</h1>")

            sections = ['posts', 'followers', 'following', 'about']
            for section in sections:
                file.write(f"<h2>{section.capitalize()} Screenshots</h2>")
                screenshot_number = 1
                while True:
                    screenshot_path = os.path.join(self.screenshot_dir, f"instagram_{section}_{screenshot_number}.png")
                    if not os.path.exists(screenshot_path):
                        break
                    file.write(f"<img src='{screenshot_path}' width='800' /><br>")
                    screenshot_number += 1

            file.write("</body></html>")
        logging.info(f"Report generated at {report_file}")

    def close(self):
        if self.driver:
            self.driver.quit()

def main():
    username = input("Enter your Instagram username: ")
    password = getpass("Enter your Instagram password: ")
    scraper = InstagramScraper(username, password)
    scraper.login()
    scraper.scrape()
    scraper.generate_report()
    scraper.close()

if __name__ == "__main__":
    main()