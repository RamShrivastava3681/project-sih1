import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class Config:
    FACEBOOK_EMAIL = os.getenv("FACEBOOK_EMAIL")
    FACEBOOK_PASSWORD = os.getenv("FACEBOOK_PASSWORD")
    TWITTER_CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
    TWITTER_CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET")
    TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
    TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")
    INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
    INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
    CHROMEDRIVER_PATH = os.getenv("CHROMEDRIVER_PATH", "drivers/chromedriver")
