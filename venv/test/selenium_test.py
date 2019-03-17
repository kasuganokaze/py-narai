from selenium import webdriver
import json

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(executable_path="/Users/kaze/tool/chromedriver", chrome_options=chrome_options)
prefs = {"profile.managed_default_content_settings.images": 2}
driver.get('https://www.qq.com/')
tags = driver.find_elements_by_tag_name("a")
for tag in tags:
    print(tag)
