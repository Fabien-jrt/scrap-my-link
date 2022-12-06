import os
from flask import Flask, request, render_template
import json

import requests
from bs4 import BeautifulSoup


def _get_links(url: str) -> list[str]:
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, "html.parser")
    res = []
    for link in soup.find_all("a"):
        res.append(link.get('href'))
    return res



app = Flask(__name__)

@app.route("/")
def render_form():
    return render_template('form.html')

@app.route("/", methods=['POST'])
def get_form():
    url = request.form['link']
    res = _get_links(url)
    return json.dumps(res)

@app.route("/scrap/<link>")
def get_links(link: str):
    url = f"https://{link}"
    res = _get_links(url)
    return json.dumps(res)

@app.route("/scrap/unsecure/<link>")
def get_links_unsecure(link: str):
    url = f"http://{link}"
    res = _get_links(url)
    return json.dumps(res)


if __name__=="__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 4444)))