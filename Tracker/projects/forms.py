from flask_wtf import FlaskForm
from Tracker import db, database
import operator
from wtforms import StringField, SubmitField, TextAreaField, DateField, HiddenField
from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from wtforms.validators import DataRequired, Length
from Tracker.helpers import CheckProfanity
from Tracker.models import User
from sqlalchemy import select, text

class ProjectForm(FlaskForm):
    title = StringField(u'title', id="form-title", validators=[DataRequired(message="Your project needs a title"), Length(min=5,max=50), CheckProfanity(), Length(max=50)])
    
    description = TextAreaField(u'Description', id="form-description", validators=[DataRequired(message="Your project needs a description"), CheckProfanity(), Length(min=5,max=200)])
                                         
    collaborate = HiddenField(id="collaborate-data", validators=[CheckProfanity()])

    deadline = DateField(validators=[DataRequired()]) 
        
    proceed = SubmitField(u'PROCEED', id="form-deadline")