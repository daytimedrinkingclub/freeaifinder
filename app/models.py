from app import db

class Tool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(200))
    description = db.Column(db.Text)
    pros = db.Column(db.Text)
    cons = db.Column(db.Text)
    website = db.Column(db.String(200))
    category = db.Column(db.String(50))

class ToolSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    website = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50), nullable=False)
