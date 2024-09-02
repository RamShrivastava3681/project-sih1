from selenium import webdriver
from fpdf import FPDF
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

class FacebookScraper:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.driver = None
        self.screenshot_dir = "assets/screenshots"
        self.report_dir = "assets/reports"
        self.setup_directories()

    def setup_directories(self):
        try:
            if not os.path.exists(self.screenshot_dir):
                os.makedirs(self.screenshot_dir)
            if not os.path.exists(self.report_dir):
                os.makedirs(self.report_dir)
        except Exception as e:
            print(f"Error setting up directories: {e}")

    def setup_driver(self):
        try:
            options = Options()
            options.add_argument("--start-maximized")
            service = Service("drivers/chromedriver.exe")  # Path to your WebDriver
            self.driver = webdriver.Chrome(service=service, options=options)
        except Exception as e:
            print(f"Error setting up WebDriver: {e}")

    def login(self):
        try:
            self.setup_driver()
            self.driver.get("https://www.facebook.com")
            
            wait = WebDriverWait(self.driver, 10)
            
            # Enter email
            email_elem = wait.until(EC.presence_of_element_located((By.NAME, "email")))
            email_elem.send_keys(self.email)
            
            # Enter password
            password_elem = self.driver.find_element(By.NAME, "pass")
            password_elem.send_keys(self.password)
            password_elem.send_keys(Keys.RETURN)
            
            # Wait for user to handle additional checkpoints manually (e.g., OTP)
            input("Press Enter after completing the login checkpoint...")
        except Exception as e:
            print(f"Error logging in: {e}")

    def get_profile_url(self):
        try:
            # Navigate to the profile page and return the URL
            self.driver.get("https://www.facebook.com/me")
            time.sleep(5)  # Adjust as needed for page load
            return self.driver.current_url
        except Exception as e:
            print(f"Error getting profile URL: {e}")

    def save_screenshot(self, section, filename):
        try:
            screenshot_path = os.path.join(self.screenshot_dir, f"facebook_{filename}.png")
            self.driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved for {section} at {screenshot_path}")
        except Exception as e:
            print(f"Error saving screenshot: {e}")

    def scroll_and_screenshot(self, section, url):
        try:
            # Navigate to the section
            self.driver.get(url)
            time.sleep(5)  # Allow time for page to load

            # Scroll down to load more content if necessary
            last_height = self.driver.execute_script("return document.body.scrollHeight")
            screenshot_number = 1

            while True:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(3)
                new_height = self.driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height

                # Capture screenshot of the current view
                self.save_screenshot(section, f"{section}_{screenshot_number}")
                screenshot_number += 1
        except Exception as e:
            print(f"Error scrolling and taking screenshots: {e}")

    def scrape(self, url):
        # Navigate to the user's profile
        self.driver.get(url)
        time.sleep(5)  # Allow time for page to load

        # Take screenshot of the main profile page
        self.save_screenshot("profile", "profile")

        # Define sections and URLs
        sections = {
            "friends": "https://www.facebook.com/me/friends",
            "about": "https://www.facebook.com/me/about",
            "posts": url
        }

        # Take screenshots of various sections
        for section, section_url in sections.items():
            self.scroll_and_screenshot(section, section_url)
    
    def generate_report(self):
        """
        Generate a report based on the scraped data.
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=24)
        pdf.cell(200, 10, txt="Facebook Scraping Report", ln=True, align='C')
        pdf.ln(10)
    
        sections = ["profile", "friends", "about", "posts"]
        for section in sections:
            pdf.set_font("Arial", size=18)
            pdf.cell(200, 10, txt=section.capitalize(), ln=True, align='L')
            pdf.ln(10)
        
            screenshot_number = 1
            while True:
                if section == "profile" and screenshot_number == 1:
                    screenshot_path = os.path.join(self.screenshot_dir, f"facebook_{section}.png")
                else:
                    screenshot_path = os.path.join(self.screenshot_dir, f"facebook_{section}_{screenshot_number}.png")

                if not os.path.exists(screenshot_path):
                    break
                
                pdf.image(screenshot_path, x=10, w=180)
                pdf.ln(85)  # Adjust space between screenshots
                screenshot_number += 1
                
        report_file = os.path.join(self.report_dir, "report.pdf")
        pdf.output(report_file)
        print(f"Report generated at {report_file}")
                
    def close(self):
        if self.driver:
            self.driver.quit()

# Example usage
if __name__ == "__main__":
    email = "your_email"
    password = "your_password"
    fb_scraper = FacebookScraper(email, password)
    fb_scraper.login()
    profile_url = fb_scraper.get_profile_url()
    fb_scraper.scrape(profile_url)
    fb_scraper.generate_report()
    fb_scraper.close()