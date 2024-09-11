from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL

class ToolSubmissionForm(FlaskForm):
    name = StringField('Tool Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    website = StringField('Website URL', validators=[DataRequired(), URL()])  # Changed from 'url' to 'website'
    category = SelectField('Category', choices=[('productivity', 'Productivity'), ('development', 'Development'), ('design', 'Design'), ('other', 'Other')])
    image_url = StringField('Image URL', validators=[DataRequired(), URL()])
    pros = TextAreaField('Pros', validators=[DataRequired()])
    cons = TextAreaField('Cons', validators=[DataRequired()])
    submit = SubmitField('Submit Tool')
