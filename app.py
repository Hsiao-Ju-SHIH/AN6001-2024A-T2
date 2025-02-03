#
# Syn code spaces is very high risk, sometimes fail

from flask import Flask
from flask import render_template, request
import textblob
import google.generativeai as genai
import os

# api = 'AIzaSyC56T9cwh1Voqaw0H7DykFsTfLtX2DzUQw'
api = os.getenv('makersuite')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/main', methods=['GET', 'POST'])
def main():
    name = request.form.get('q')
    return render_template('main.html')

@app.route('/SA', methods=['GET', 'POST'])
def SA():
    return render_template('SA.html')

@app.route('/paynow', methods=['GET', 'POST'])
def paynow():
    return render_template('paynow.html')

@app.route('/SA_result', methods=['GET', 'POST'])
def SA_result():
    q = request.form.get('q')
    r = textblob.TextBlob(q).sentiment
    return render_template('SA_result.html', r=r)

@app.route('/GenAI', methods=['GET', 'POST'])
def GenAI():
    return render_template('GenAI.html')

@app.route('/GenAI_result', methods=['GET', 'POST'])
def GenAI_result():
    q = request.form.get('q')
    genai.configure(api_key=api)
    model = genai.GenerativeModel('gemini-1.5-flash')
    r = model.generate_content(q)
    r = r.candidates[0].content.parts[0].text
    return render_template('GenAI_result.html', r=r)

if __name__ == '__main__':
    app.run(port=1234)