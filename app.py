import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify

import json

app = Flask(__name__)
@app.route("/")
def index():
    return "this is a simple imgur api with web scraping . \n You can use this by passing gallery id in the url of this website \n. for example : https://imgur-api-scraper.herokuapp.com/{gallery_id}"
@app.route("/<gallery_id>")
def hello_world(gallery_id):
    
    url = f'https://imgur.com/gallery/{gallery_id}'
    response = requests.get(url)

    soup = BeautifulSoup(response.content,'html.parser')

    data = soup.find('script')
    data = data.text
    data = data.replace('<script>', '')
    data = data.replace("\\" , '')
    data = data.replace('window.postDataJSON=' , '')
    data = data[1:-1]
    data = data.replace('\n' , '')
    try:
        data = json.loads(data)
    except:
        print('there was an error so just returniing string non formatted json')
    return jsonify(data)
    


if __name__ == '__main__':
   app.run(host="localhost",port=8800, debug=  True)


