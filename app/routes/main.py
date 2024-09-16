from flask import Blueprint, render_template
from app import supabase

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    try:
        response = supabase.table('tool').select("*").execute()
        tools = response.data
        return render_template('main/tools.html', tools=tools)
    except Exception as e:
        return f"Error: {str(e)}", 500