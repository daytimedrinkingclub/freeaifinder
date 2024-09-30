from app import create_app
from flask import Flask

app = create_app()

if __name__ == '__main__':
    extra_files = [
        './app/templates/',  # Monitor all files in the templates directory
    ]
    app.run(debug=True, extra_files=extra_files)