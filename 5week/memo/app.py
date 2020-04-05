import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/memo')
def memo_post():
  url_received = request.form.get('url', None)
  comment_received = request.form.get('comment', '')

  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
  data = requests.get(url_received, headers=headers)
  soup = BeautifulSoup(data.text, 'html.parser')

  og_title = soup.select_one('meta[property="og:title"]')
  og_description = soup.select_one('meta[property="og:description"]')
  og_image = soup.select_one('meta[property="og:image"]')

  return

if __name__ == "__main__":
  app.run('0.0.0.0', port=5000, debug=True)