"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, flash, session, abort
from werkzeug.utils import secure_filename
import datetime
from .forms import *

###
# Routing for your application.
###
@app.route('/')
def about():
    return render_template('about.html', name="Neko Reid")

@app.route('/profile', methods=['POST', 'GET'])
def profile():
    myform = addProfile()
    # Validate file upload on submit
    if request.method == 'POST':
        if myform.validate_on_submit():
            f = myform.photo.data
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File Saved', 'success')
    return render_template('profile.html', form = myform)
#, joined=format_date_joined(datetime.datetime.now())

@app.route('/profiles')
def profiles():
    """Render website's profiles page."""
    return render_template('profiles.html')


###
# The functions below should be applicable to all Flask apps.
###

def format_date_joined(date):
    return  date.strftime("%B, %Y") 

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
