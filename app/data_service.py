from app.models import Tool, ToolSubmission
from app import db

def get_tools():
    return Tool.query.with_entities(
        Tool.id,
        Tool.name,
        Tool.image_url,
        Tool.description,
        Tool.pros,
        Tool.cons,
        Tool.website,
        Tool.category
    ).all()

def create_tool_submission(name, description, website, category):
    tool_submission = ToolSubmission(
        name=name,
        description=description,
        website=website,
        category=category
    )
    db.session.add(tool_submission)
    db.session.commit()

def get_tool_by_id(tool_id):
    return Tool.query.get(tool_id)
