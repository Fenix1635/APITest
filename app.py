from flask import Flask
from flask_cors import CORS
import requests
import json
import os
from selenium import webdriver
from bs4 import BeautifulSoup, element
import pandas as pd

app = Flask(__name__)

cors = CORS(app, resource={r"/*":{"origins": "*"}})



@app.route('/', methods=['GET'])

def index():
    return "<h1>Olá<h1>"

@app.route('/api', methods=['GET'])
def deploy():
    test = []
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get('https://www.catch.com.au/product/asus-rog-strix-geforce-rtx-3090-24gb-oc-edition-graphics-card-7126834/?sid=rtx%203090&sp=1&st=32&srtrev=sj-x57l6dk9opvxnkkz8gmflc')
    try:
        element = driver.find_element_by_xpath("/html/body/main/section[2]/article[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div")
        content = element.get_attribute("innerText")
        test.append(content)

        element2 = driver.find_element_by_xpath("//*[@id='form-cart-add']/section[2]/div/div[2]/button")
        content2 = element2.get_attribute("innerText")
        test.append(content2)
        return test
    except:
        test = 0
        return test
    

def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    print('ONLINE')
    main()