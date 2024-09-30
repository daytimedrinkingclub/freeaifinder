from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from app import supabase
from urllib.parse import urlparse, urlunparse, parse_qsl, urlencode

bp = Blueprint('main', __name__)

def add_utm_params(url, **params):
    parsed_url = urlparse(url)
    query_params = dict(parse_qsl(parsed_url.query))
    utm_params = {f"utm_{k}": v for k, v in params.items()}
    query_params.update(utm_params)
    new_query = urlencode(query_params)
    return urlunparse(
        (parsed_url.scheme, parsed_url.netloc, parsed_url.path, 
         parsed_url.params, new_query, parsed_url.fragment)
    )

@bp.route('/')
def index():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = 30
        
        response = supabase.table('tool').select("*").order('created_at', desc=True).range(
            (page - 1) * per_page, 
            page * per_page - 1
        ).execute()
        
        tools = response.data
        
        # Fetch all unique categories for the category navigation
        categories_response = supabase.table('tool').select('category').execute()
        categories = list(set(tool['category'] for tool in categories_response.data))
        
        # Add UTM parameters to tool links
        for tool in tools:
            tool['link'] = add_utm_params(tool['link'], 
                                          source='free_ai_finder', 
                                          medium='directory', 
                                          campaign='tool_listing', 
                                          content=tool['name'].lower().replace(' ', '-'))
        
        return render_template('main/tools.html', 
                               tools=tools, 
                               page=page, 
                               categories=categories,
                               meta_description="Explore our curated list of free AI tools to enhance your productivity and creativity.")
    except Exception as e:
        current_app.logger.error(f"Error fetching tools: {str(e)}")
        return render_template('error.html', error_message="An error occurred while fetching the tools. Please try again later."), 500

@bp.route('/submit-tool', methods=['GET', 'POST'])
def submit_tool():
    if request.method == 'POST':
        tool_name = request.form['tool_name']
        description = request.form['description']
        website = request.form['website']
        category = request.form['category']
        creator_email = request.form['creator_email']
        try:
            data, count = supabase.table('submitted_tools').insert({
                "name": tool_name,
                "description": description,
                "link": website,
                "category": category,
                "email": creator_email
            }).execute()
            
            if count == 1:
                flash('Tool submitted successfully! It will be reviewed before being added to the directory.', 'success')
            else:
                flash('Error submitting tool. Please try again.', 'error')
        except Exception as e:
            current_app.logger.error(f"Error submitting tool: {str(e)}")
            flash('An error occurred while submitting the tool. Please try again.', 'error')
        
        return redirect(url_for('main.index'))
    
    return render_template('main/submit_tool.html',
                           meta_description="Contribute to our free AI tools directory by submitting your favorite AI tool. Help others discover useful AI solutions.")

@bp.route('/tool/<int:tool_id>')
def tool_details(tool_id):
    try:
        response = supabase.table('tool').select("*").eq('id', tool_id).execute()
        
        if not response.data:
            return render_template('error.html', error_message="Tool not found."), 404
        
        tool = response.data[0]
        
        # Add UTM parameters to tool link
        tool['link'] = add_utm_params(tool['link'], 
                                      source='free_ai_finder', 
                                      medium='tool_details', 
                                      campaign='tool_page', 
                                      content=tool['name'].lower().replace(' ', '-'))
        
        return render_template('main/tool_details.html', tool=tool)
    except Exception as e:
        current_app.logger.error(f"Error fetching tool details: {str(e)}")
        return render_template('error.html', error_message="An error occurred while fetching the tool details. Please try again later."), 500
    
@bp.route('/category/<string:category_name>')
def category(category_name):
    try:
        page = request.args.get('page', 1, type=int)
        per_page = 30
        
        response = supabase.table('tool').select("*").eq('category', category_name).order('created_at', desc=True).range(
            (page - 1) * per_page, 
            page * per_page - 1
        ).execute()
        
        tools = response.data
        
        # Fetch all unique categories for the category navigation
        categories_response = supabase.table('tool').select('category').execute()
        categories = list(set(tool['category'] for tool in categories_response.data))
        
        # Add UTM parameters to tool links
        for tool in tools:
            tool['link'] = add_utm_params(tool['link'], 
                                          source='free_ai_finder', 
                                          medium='category_page', 
                                          campaign='tool_listing', 
                                          content=tool['name'].lower().replace(' ', '-'))
        
        return render_template('main/category.html', 
                               tools=tools, 
                               page=page, 
                               categories=categories,
                               current_category=category_name,
                               meta_description=f"Explore our curated list of free AI tools in the {category_name} category.")
    except Exception as e:
        current_app.logger.error(f"Error fetching tools for category {category_name}: {str(e)}")
        return render_template('error.html', error_message="An error occurred while fetching the tools. Please try again later."), 500