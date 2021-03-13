import flask
from flask import request
import requests
import json

app = flask.flask(__name__)


try: 
    url = 'https://www.coupang.com/vp/products/4348473678/vendor-items/72771319696/shipping-consolidation-widget?vendorId=A00157129&shippingPlaceId=657033'


    headers = {
                'authority': 'www.coupang.com',
                "pragma": "no-cache",
                'cache-control': 'no-cache',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
                'accept': '*/*',
                'sec-fetch-dest':'empty',
                'sec-fetch-mode':'cors',
                'sec-fetch-site':'same-origin',
                'referer': 'https://www.coupang.com//vp/products/4348473678?vendorItemId=72771319696&sourceType=SDP_SC_RECOMMENDATION'
            }

    response = requests.get(url, headers=headers)
    response_formatted2 = json.loads(response.content.decode('utf-8-sig').encode('utf-8'))
except: 
    print('ERROR')



@app.route('/', methdos=['GET'])

def home():
    
    return response_formatted2