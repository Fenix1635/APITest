from flask import Flask
from flask_cors import CORS
import requests
import json
import os

app = Flask(__name__)

cors = CORS(app, resource={r"/*":{"origins": "*"}})

 
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



@app.route('/', methods=['GET'])

def index():
    return "<h1>Olá<h1>"

@app.route('/api', methods=['GET'])
def deploy():
    return response_formatted2

def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    print('ONLINE')
    main()