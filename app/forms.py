from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from app.models import Resort

# Define class for location form
class LocateForm(FlaskForm):
	# Create address field
	address = StringField('Enter Address Below', validators=[DataRequired()])
	# Create submission button
	submit = SubmitField('Submit')

# Define class for comment form
class CommentForm(FlaskForm):
	# Refine choices for drop-down menu from db
	choices = [(r.resortname, r.resortname) for r in Resort.query.order_by('resortname').all()]
	#choices=[('Aspen', 'Aspen'), ('Alyeska', 'Alyeska'), ('Arizona Snow Bowl', 'Arizona Snow Bowl')]
	# Create drop-down menu
	comment_resort = SelectField('Select Resort:', choices=choices)
	# Create comment field
	comment = TextAreaField('Enter Comments Here:', validators=[DataRequired()])
	# Create submission button
	submit = SubmitField('Submit')
