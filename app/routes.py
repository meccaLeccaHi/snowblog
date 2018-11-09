from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import LocateForm, CommentForm
from app.models import Resort, Post
from scipy.spatial import distance
import googlemaps
from config import Config
import numpy as np

# 'Home' view
@app.route('/')
@app.route('/index')
def index():

	# Get list of all posts
	posts = Post.query.all()
	
	# Render them in webpage
	return render_template('index.html', title='Home', posts=posts)


# 'Locate ski resorts' view
@app.route('/locate', methods=['GET', 'POST'])
def locate():
	# Get data from form
	form = LocateForm()
	# Check validity
	if form.validate_on_submit():
		gmaps = googlemaps.Client(key=Config.GOOGLE_KEY)
		
		# Geocode address w/ Google API
		geocoding_results = gmaps.geocode(form.address.data)
		user_loc = geocoding_results[0]['geometry']['location']
		
		# Collect resort position data
		resort_locs = [(i.latitude, i.longitude) for i in Resort.query.all()]

		# Calculate the euclidean distance to each
		dist = np.array([distance.euclidean(rl, (user_loc['lat'], user_loc['lng'])) for rl in resort_locs])

		# Sort and select 5 closest options
		results = [Resort.query.get(int(i)) for i in dist.argsort()[:5][::-1]]

	else:
		results=[]

	return render_template('locate.html', title="Find resorts", form=form, results=results)

# 'Comment' view
@app.route('/comment', methods=['GET', 'POST'])
def comment():
	# Get data from form
	form = CommentForm()
	# Check validity
	if form.validate_on_submit():

		# Add comments to database
		post = Post(body=form.comment.data, resortname=form.comment_resort.data)
		db.session.add(post)
		db.session.commit()

		# Provide user feedback and re-direct to 'Home' view
		flash('Your feedback is now live!')
		return redirect(url_for('index'))

	return render_template('comment.html', title="Share your experiences", form=form)
