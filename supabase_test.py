from supabase import create_client, Client
import os

# Supabase configuration
url: str = "https://supabasekong-y4wgo88ksgckw40kows84o0g.badalhibadal.com/"
key: str = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzdXBhYmFzZSIsImlhdCI6MTcyNjQ4MTM0MCwiZXhwIjo0ODgyMTU0OTQwLCJyb2xlIjoiYW5vbiJ9.WGBYl_bJ6tHbcZ1Ha8eyGLjRp3tFok8iKqm_FDMI2ec"

supabase: Client = create_client(url, key)

try:
    # Insert a test entry
    test_tool = {
        "name": "Test Tool",
        "description": "This is a test tool entry",
        "link": "https://example.com",
        "category": "Test"
    }
    insert_response = supabase.table('tool').insert(test_tool).execute()
    print("Inserted test tool:")
    print(insert_response.data)

    # Retrieve all tools
    response = supabase.table('tool').select("*").execute()
    print(f"\nSuccessfully retrieved {len(response.data)} tools:")
    for tool in response.data:
        print(tool)
except Exception as e:
    print(f"Error: {str(e)}")