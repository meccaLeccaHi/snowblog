from datetime import datetime
from app import db


class Resort(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	resortname = db.Column(db.String(64), index=True, unique=True)
	state = db.Column(db.String(2))
	latitude = db.Column(db.Integer)
	longitude = db.Column(db.Integer)
	url = db.Column(db.String(128))

	def __repr__(self):
		return '<Resort {}>'.format(self.resortname)


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(140))
	resortname = db.Column(db.String(64), index=True, unique=True)

	def __repr__(self):
		return '<Post {}>'.format(self.body)
