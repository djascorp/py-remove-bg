from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return 'About Page Route'


@app.route('/portfolio')
def portfolio():
    return 'Portfolio Page Route'


@app.route('/contact')
def contact():
    return 'Contact Page Route'

app.run()
# @app.route('/api')
# def api():
#     with open('data.json', mode='r') as my_file:
#         text = my_file.read()
#         return text