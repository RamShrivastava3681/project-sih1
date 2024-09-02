# project-sih
During investigation when the social media accounts of accused/suspect are opened for examination or creating Panchnamas, it would be better if some tool is designed which can automatically parse the data and provide the screenshot of the posts, messages, timeline, friend list, following, followers, account info, etc and provide screenshots in a documented form. * The examiner may choose to print the screenshots as per requirements. This will omit any human error during the process and also help to thoroughly reviewing the data found for the said social media account. * Separate options for Facebook, Twitter, Instagram, Telegram, WhatsApp, Google account etc may be provided in the tool. * Many a times, the social media accounts do not open in Desktops even if we have the right credentials and the examiner have to use a dummy android phone. So, two separate versions (Android and windows) of this tool will be helpful.

##Acknowledgements
This tool is designed to facilitate the investigation process by automating the extraction and documentation of data from various social media platforms. It aims to:

Automate Data Parsing: The tool parses data from social media accounts, including posts, messages, timelines, friend lists, following lists, followers, and account information.
Provide Screenshots: It captures and documents screenshots of the data in a structured format, which can be printed or reviewed as needed. This helps in minimizing human error during the documentation process.
Support Multiple Platforms: Options are provided for different social media platforms, including Facebook, Twitter, Instagram, Telegram, WhatsApp, and Google accounts.
Compatibility with Devices: The tool includes separate versions for Android and Windows to accommodate situations where social media accounts may only be accessible via mobile devices.
This tool is intended to enhance the efficiency and accuracy of social media data collection during investigations, ensuring thorough and reliable documentation.

## API Reference

#1. Facebook
Selenium: A web automation tool that can be used to interact with Facebook's web interface to extract data. However, scraping Facebook directly is against their terms of service.

Selenium Documentation
BeautifulSoup + Requests: For parsing HTML content if you're scraping specific pages. Be cautious of Facebook's anti-scraping measures.

BeautifulSoup Documentation
Requests Documentation
2. Twitter
Tweepy: A Python library for accessing Twitter's API and collecting tweets, user information, etc.

Tweepy Documentation
Snscrape: A library to scrape data from Twitter without using the API, useful for gathering historical data.

Snscrape Documentation
3. Instagram
Instaloader: A tool to download Instagram photos, videos, and metadata from profiles.

Instaloader Documentation
Instagram Scraper: A Python tool for scraping Instagram posts and user profiles.

Instagram Scraper GitHub Repository
4. Telegram
Telethon: A Python library to interact with Telegram’s API and scrape messages, user information, and more.

Telethon Documentation
Pyrogram: Another Python library for interacting with Telegram’s API, supporting both user and bot accounts.

Pyrogram Documentation
5. WhatsApp
WhatsApp Web Scraper: Tools for automating WhatsApp Web interactions. Note that official APIs are preferred for structured data access.
WhatsApp Web Scraper GitHub Repository (Baileys for WhatsApp Web)
6. Google Accounts
Google API Client Libraries: For accessing Google data via APIs, such as the People API.
Google API Client Libraries Documentation
For each platform, always review and adhere to their terms of service and policies regarding data scraping. Where possible, use official APIs to ensure compliance and data accuracy.









