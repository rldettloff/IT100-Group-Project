import os
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    links = []
    images = os.listdir(os.path.join(os.path.dirname(__file__), 'static'))
    for item in images:
        links.append(url_for('static', filename=item))
    return render_template('home.html', links=links)

@app.route('/historical')
def historical_art():
    return render_template('historical.html')

@app.route('/submitted')
def user_art():
    return render_template('user.html')

@app.route('/share', methods=['GET','POST'])
def share():
    
    return render_template('share.html')

@app.route('/aboutus')
def about_us():
    return render_template('aboutus.html')

if __name__ == '__main__':
    app.run(debug=True)
