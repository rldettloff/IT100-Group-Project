import os
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def gallery():
    links = []
    images = os.listdir(os.path.join(os.path.dirname(__file__), 'static'))
    for item in images:
        links.append(url_for('static', filename=item))
    return render_template('gallery.html', links=links)

if __name__ == '__main__':
    app.run(debug=True)
