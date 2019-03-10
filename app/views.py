"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
from app import app, db
from flask import render_template, request, redirect, url_for, flash, session, abort
from forms import addProfile
from models import UserProfile
from werkzeug.utils import secure_filename
import datetime
from .forms import *
import os

###
# Routing for your application.
###
@app.route('/')
def home():
    flash('Hello!.\nTo begin, you may click profile above to add a new profile.', 'success')
    return render_template('home.html')
    
@app.route('/about')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/profile', methods=['POST'])
@app.route('/profile/<userid>', methods=['GET'])
def profile(userid=None):
    myform = addProfile()
    # Validate file upload on submit
    if request.method == 'POST' and myform.validate_on_submit():
        fname = myform.fname.data
        lname = myform.lname.data
        gender = myform.gender.data
        email = myform.email.data
        location = myform.location.data
        biography = myform.biography.data
        
        new = UserProfile(fname, lname, gender, email, location, biography)

        db.session.add(new)
        db.session.commit()
        
        propic = myform.propic.data

        propic.save(os.path.join(app.config['UPLOAD_FOLDER'], new.get_id()))
        new.updateProPic( 'pro-pics/'+ new.get_id() )
        db.session.commit()
        
        flash('Profile Successfully Added', 'success')
        return redirect(url_for('profiles'))
    elif request.method == 'GET':
        u = UserProfile.query.filter_by(id=int(userid)).first_or_404()
        return render_template('user.html', user=u)
            
    return render_template('profile.html', form = myform)

@app.route('/profiles')
def profiles():
    """Render website's profiles page."""
    userslst = UserProfile.query.all()
    return render_template('profiles.html', users=userslst)


###
# The functions below should be applicable to all Flask apps.
###

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
