from app.models import Tool, ToolSubmission
from app import db

def get_tools():
    return Tool.query.all()

def create_tool_submission(form):
    tool_submission = ToolSubmission(
        name=form.name.data,
        description=form.description.data,
        website=form.website.data,
        category=form.category.data
    )
    db.session.add(tool_submission)
    db.session.commit()
