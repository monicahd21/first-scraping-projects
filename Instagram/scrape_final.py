# FINAL INSTAGRAM WEB SCRAPER FOR NAFNAF BASED ON URL

import selenium
import parser_libraries
from selenium import webdriver
from selenium.webdriver import Chrome
from instascrape import Profile, scrape_posts, Post, Hashtag
import time

headers = {
    "user-agent": "Chrome/87.0.4389.23",
    "cookie": "sessionid= "
}

f = open('input_data.txt', 'r')
posts_codes = []

for line in f:
    line = line.split(':')[1]
    line = line.split('-')
    if (len(line) == 4):
        line = line[0].strip(' ')
    else:
        line = line[0].strip(' ')+'-'+line[1].strip(' ')
    posts_codes.append(line)

print(posts_codes)
nafnaf = Profile('nafnafcol')
nafnaf.scrape(headers=headers)

for i in range(len(posts_codes)):
    nafnaf_post = Post(posts_codes[i])
    nafnaf_post.scrape()
    print('----------------------')
    print(nafnaf_post.to_dict()['caption'])
    time.sleep(10)
