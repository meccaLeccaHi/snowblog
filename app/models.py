from datetime import datetime
from app import db

# Define 'Resort' table
class Resort(db.Model):
	# Define table columns
	id = db.Column(db.Integer, primary_key=True)
	resortname = db.Column(db.String(64), index=True, unique=True)
	state = db.Column(db.String(2))
	latitude = db.Column(db.Integer)
	longitude = db.Column(db.Integer)
	url = db.Column(db.String(128))

	# Define the representation of instances of this class
	def __repr__(self):
		return '<Resort {}>'.format(self.resortname)

# Define 'Post' table
class Post(db.Model):
	# Define table columns
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(140))
	resortname = db.Column(db.String(64), index=True, unique=True)

	# Define the representation of instances of this class
	def __repr__(self):
		return '<Post {}>'.format(self.body)
