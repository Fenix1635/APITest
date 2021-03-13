from flask import Flask
from flask_cors import CORS
import requests
import json
import os
from selenium import webdriver

app = Flask(__name__)

cors = CORS(app, resource={r"/*":{"origins": "*"}})

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
driver.get('https://www.catch.com.au/product/asus-rog-strix-geforce-rtx-3090-24gb-oc-edition-graphics-card-7126834/?sid=rtx%203090&sp=1&st=32&srtrev=sj-x57l6dk9opvxnkkz8gmflc')
test = driver.page_source

@app.route('/', methods=['GET'])

def index():
    return "<h1>Olá<h1>"

@app.route('/api', methods=['GET'])
def deploy():
    return test

def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    print('ONLINE')
    main()