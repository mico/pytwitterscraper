from flask import Flask
from flask import request
from pytwitterscraper import TwitterScraper
tw = TwitterScraper()

app = Flask(__name__)


@app.route('/')
def hello_world():
    return """<h4></h4>
              <div style="padding: 20px; text-align: center; width: 100%;">
              <form action="/scrape_tweet" method="get">
              <input name="tweet_url" size="60" placeholder="enter a tweet link">
              <button type="submit">scrape tweet</button></form></div>
              """


@app.route('/scrape_tweet')
def scrape_tweet():
    tweet_id = request.args['tweet_url'].split('/')[-1]
    comments = tw.get_tweet_comments_page(tweet_id)
    return "<h4>scrape results</h4>"\
        "<table border='1'>" \
        "<tr><th>List Item</th><th>Likes</th></tr>"\
        "<tr>" +\
        '</tr><tr>'.join(
            [f"<td>{comment['full_text']}</td><td>{comment['favorite_count']}</td>" for comment in comments.values()]) +\
        "</tr></table>"
