from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
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
    
@bp.route('/submit-tool', methods=['GET', 'POST'])
def submit_tool():
    if request.method == 'POST':
        # Process the form submission
        tool_name = request.form['tool_name']
        description = request.form['description']
        website = request.form['website']
        category = request.form['category']
        
        # Insert the new tool into the Supabase submitted_tools table
        try:
            data, count = supabase.table('submitted_tools').insert({
                "name": tool_name,
                "description": description,
                "link": website,
                "category": category
            }).execute()
            
            if count == 1:
                flash('Tool submitted successfully! It will be reviewed before being added to the directory.', 'success')
            else:
                flash('Error submitting tool. Please try again.', 'error')
        except Exception as e:
            current_app.logger.error(f"Error submitting tool: {str(e)}")
            flash('An error occurred while submitting the tool. Please try again.', 'error')
        
        return redirect(url_for('main.index'))
    
    return render_template('main/submit_tool.html')
