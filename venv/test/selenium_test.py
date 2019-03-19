from selenium import webdriver
import json

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(executable_path="/Users/kaze/tool/chromedriver", chrome_options=chrome_options)
driver.get('https://detail.tmall.com/item.htm?spm=a220o.1000855.0.da321h.17f32a4fJzPKPF&id=579794586729&sku_properties=10004:709990523;5919063:6536025')
tags = driver.find_elements_by_class_name("tm-sale-prop")
for tag in tags:
    print(tag.text)
