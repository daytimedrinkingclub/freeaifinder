from flask import Blueprint, render_template, redirect, url_for, abort
from app.forms import ToolSubmissionForm
from app.data_service import get_tools, create_tool_submission, get_tool_by_id
from app.models import Tool

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    tools = get_tools()
    return render_template('home/hero.html', tools=tools)

@bp.route('/submit', methods=['GET', 'POST'])
def submit_tool():
    form = ToolSubmissionForm()
    if form.validate_on_submit():
        create_tool_submission(form.name.data, form.description.data, form.website.data, form.category.data)
        return redirect(url_for('main.index'))
    return render_template('pages/submit_tool.html', form=form)

@bp.route('/tool/<int:tool_id>')
def tool_details(tool_id):
    tool = get_tool_by_id(tool_id)  # You need to implement this function in data_service.py
    if tool is None:
        abort(404)  # Tool not found
    return render_template('pages/details.html', tool=tool)


@bp.route('/about')
def about():
    return render_template('pages/about.html')