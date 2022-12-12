import os
from flask import Flask, render_template, url_for
from utils import process_file, save_picture
from forms import ArtForm

app = Flask(__name__)
app.secret_key = '3d6f45a5fc12445dbac2f59c3b6c7cb1'


@app.route('/')
@app.route('/home')
def home():
    """Home

    Returns:
        Homepage
    """
    content = []
    images = os.listdir(os.path.join(os.path.dirname(__file__), 'static/historical'))
    for image in images:
        content.append(url_for('static', filename='historical/'+image))
    return render_template('home.html', links=content)

@app.route('/historical')
def historical_art():
    """Historical art page

    Returns:
        Hisorical
    """
    content = []
    images = os.listdir(os.path.join(os.path.dirname(__file__), 'static/historical'))
    for image in images:
        content.append(process_file(image,'historical'))
    return render_template('historical.html', content=content)

@app.route('/submitted')
def user_art():
    """User submitted art page

    Returns:
        User submissions
    """
    content = []
    images = os.listdir(os.path.join(os.path.dirname(__file__), 'static/submitted'))
    for image in images:
        content.append(process_file(image,'submitted'))
    return render_template('user.html', content=content)

@app.route('/share', methods=['GET','POST'])
def share():
    form = ArtForm()
    if form.validate_on_submit():
        if form.picture.data:
            save_picture(form.picture.data, form.title.data, form.artist.data)
    return render_template('share.html', form=form)

@app.route('/aboutus')
def about_us():
    return render_template('aboutus.html')

if __name__ == '__main__':
    app.run(debug=True)
