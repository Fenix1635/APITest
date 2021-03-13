import requests
import json
import os
from selenium import webdriver


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
driver.get('https://www.catch.com.au/product/asus-rog-strix-geforce-rtx-3090-24gb-oc-edition-graphics-card-7126834/?sid=rtx%203090&sp=1&st=32&srtrev=sj-x57l6dk9opvxnkkz8gmflc')
print(driver.page_source)

