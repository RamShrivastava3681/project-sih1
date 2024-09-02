import os
import sys
from getpass import getpass
from facebook_scraper import FacebookScraper
from instagram_scraper import InstagramScraper
from twitter_scraper import TwitterScraper

def main():
    print("Select the platform to scrape:")
    print("1. Facebook")
    print("2. Instagram")
    print("3. Twitter")

    while True:
        try:
            choice = int(input("Enter your choice (1/2/3): "))
            if choice in [1, 2, 3]:
                break
            else:
                print("Invalid choice. Please choose a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    platforms = {
        1: FacebookScraper,
        2: InstagramScraper,
        3: TwitterScraper
    }

    email = input("Enter the email/username: ")
    password = getpass("Enter the password: ")

    scraper = platforms[choice](email, password)

    try:
        scraper.login()
        
        # Automatically detect and use the logged-in user's profile URL
        profile_url = scraper.get_profile_url()
        scraper.scrape(profile_url)

        # Generate a report with the screenshots
        scraper.generate_report()

        print("Scraping and report generation completed successfully.")

    except Exception as e:
        print(f"An error occurred during scraping: {e}")

    finally:
        scraper.close()

if __name__ == "__main__":
    main()