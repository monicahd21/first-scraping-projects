# URL INSTAGRAM WEB SCRAPER FOR NAFNAF

import selenium
import parser_libraries
from selenium import webdriver
from selenium.webdriver import Chrome
from instascrape import Profile, scrape_posts

path = "C:/Users/Moni/Downloads/chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://www.instagram.com/")
webdriver = Chrome("C:/Users/Moni/Downloads/chromedriver.exe")

headers = {
    "user-agent": "Chrome/87.0.4389.23",
    "cookie": "sessionid= "
}

nafnaf = Profile("nafnafcol")
nafnaf.scrape(headers=headers)
posts = nafnaf.get_posts(webdriver=webdriver, login_first=True, amount=20)
scraped_posts, unscraped_posts = scrape_posts(
    posts, headers=headers, pause=5, silent=False)
