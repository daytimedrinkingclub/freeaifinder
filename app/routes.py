from flask import Blueprint, render_template, redirect, url_for
from app.forms import ToolSubmissionForm
from app.data_service import get_tools, create_tool_submission

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    tools = get_tools()
    return render_template('home/index.html', tools=tools)
