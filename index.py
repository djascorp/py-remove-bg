from flask import Flask, render_template, redirect, url_for, request
from remover import remover

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        input_path = "./uploaded/" + str(f.filename)
        f.save(input_path)
        remover(input_path, output_path='out.png')
        return 'file uploaded successfully'


@app.route('/about')
def about():
    return 'About Page Route'


@app.route('/portfolio')
def portfolio():
    return 'Portfolio Page Route'


@app.route('/contact')
def contact():
    return 'Contact Page Route'


app.run("0.0.0.0:80")

# @app.route('/api')
# def api():
#     with open('data.json', mode='r') as my_file:
#         text = my_file.read()
#         return text
