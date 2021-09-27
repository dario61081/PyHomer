import os
from flask import Flask, render_template

app = Flask(__name__)
app.jinja_env.cache = {}
app.secret_key = os.urandom(12345)


@app.context_processor
def context_processor():
     return dict(appname="PyHomer")


@app.route('/')
def home():
     return render_template('home.html')


if __name__ == '__main__':
     app.run(host='0.0.0.0', port=os.getenv("PORT", 1234), debug=os.getenv("DEBUG", True))
