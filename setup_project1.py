#!/usr/bin/env python3
"""
Flask Multi-Page Application Setup Script
Creates all necessary files and directories for a Flask app with 11 pages
"""

import os

def create_directory_structure():
    """Create the required directory structure"""
    directories = ['templates', 'static/css', 'static/js']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")

def create_app_py():
    """Create the main Flask application file"""
    content = '''from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import os

app = Flask(__name__)

# Ensure log file exists
LOG_FILE = 'submissions.log'

def log_submission(page, username, password):
    """Log submission to terminal and file"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] Page: {page} | Username: {username} | Password: {password}\\n"
    
    # Print to terminal
    print(log_entry.strip())
    
    # Append to log file
    with open(LOG_FILE, 'a') as f:
        f.write(log_entry)

@app.route('/')
def index():
    """Main index page with links to all pages"""
    return render_template('index.html')

@app.route('/page<int:page_num>', methods=['GET', 'POST'])
def page(page_num):
    """Handle pages 1-11 with login forms"""
    if page_num < 1 or page_num > 11:
        return "Page not found", 404
    
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        log_submission(f'page{page_num}', username, password)
        return redirect(url_for('page', page_num=page_num))
    
    return render_template(f'page{page_num}.html', page_num=page_num)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
'''
    with open('app.py', 'w') as f:
        f.write(content)
    print("Created: app.py")

def create_base_template():
    """Create the base HTML template"""
    content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Flask Multi-Page App{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <nav class="navbar">
        <a href="{{ url_for('index') }}" class="nav-brand">Multi-Page App</a>
        <div class="nav-links">
            <a href="{{ url_for('index') }}">Home</a>
        </div>
    </nav>
    
    <main class="container">
        {% block content %}{% endblock %}
    </main>
    
    <footer>
        <p>&copy; 2024 Flask Multi-Page App</p>
    </footer>
</body>
</html>
'''
    with open('templates/base.html', 'w') as f:
        f.write(content)
    print("Created: templates/base.html")

def create_index_template():
    """Create the index page template"""
    content = '''{% extends "base.html" %}

{% block title %}Home - Flask Multi-Page App{% endblock %}

{% block content %}
<div class="hero">
    <h1>Welcome to Flask Multi-Page App</h1>
    <p>Navigate to any of the 11 pages below</p>
</div>

<div class="page-grid">
    {% for i in range(1, 12) %}
    <div class="page-card">
        <h3>Page {{ i }}</h3>
        <p>Access page {{ i }} content and login</p>
        <a href="{{ url_for('page', page_num=i) }}" class="btn">Visit Page {{ i }}</a>
    </div>
    {% endfor %}
</div>

<div class="info-section">
    <h2>About This App</h2>
    <p>This Flask application demonstrates:</p>
    <ul>
        <li>Main index page with navigation to 11 sub-pages</li>
        <li>Individual login forms on each page</li>
        <li>Logging submissions to both terminal and file</li>
        <li>Responsive design with modern CSS</li>
    </ul>
</div>
{% endblock %}
'''
    with open('templates/index.html', 'w') as f:
        f.write(content)
    print("Created: templates/index.html")

def create_page_templates():
    """Create templates for pages 1-11"""
    for i in range(1, 12):
        prev_page = i - 1
        next_page = i + 1
        
        content = '''{% extends "base.html" %}

{% block title %}Page ''' + str(i) + ''' - Flask Multi-Page App{% endblock %}

{% block content %}
<div class="page-header">
    <h1>Page ''' + str(i) + '''</h1>
    <p>This is page ''' + str(i) + ''' of the multi-page application</p>
</div>

<div class="content-section">
    <h2>Content for Page ''' + str(i) + '''</h2>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
    <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
</div>

<div class="login-section">
    <h2>Login to Page ''' + str(i) + '''</h2>
    <form method="POST" class="login-form">
        <div class="form-group">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>
        </div>
        <div class="form-group">
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
        </div>
        <button type="submit" class="btn">Submit</button>
    </form>
</div>

<div class="navigation">
    <a href="{{ url_for('index') }}" class="btn btn-secondary">Back to Home</a>
'''
        
        if i > 1:
            content += '    <a href="{{ url_for(\'page\', page_num=' + str(prev_page) + ') }}" class="btn btn-secondary">Previous Page</a>\n'
        
        if i < 11:
            content += '    <a href="{{ url_for(\'page\', page_num=' + str(next_page) + ') }}" class="btn btn-secondary">Next Page</a>\n'
        
        content += '''</div>
{% endblock %}
'''
        
        with open(f'templates/page{i}.html', 'w') as f:
            f.write(content)
        print(f"Created: templates/page{i}.html")

def create_css():
    """Create the CSS stylesheet"""
    content = '''/* Reset and Base Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
    color: #333;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

/* Navigation */
.navbar {
    background: rgba(255, 255, 255, 0.95);
    padding: 1rem 2rem;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.nav-brand {
    font-size: 1.5rem;
    font-weight: bold;
    color: #667eea;
    text-decoration: none;
}

.nav-links a {
    color: #333;
    text-decoration: none;
    margin-left: 2rem;
    transition: color 0.3s;
}

.nav-links a:hover {
    color: #667eea;
}

/* Hero Section */
.hero {
    text-align: center;
    padding: 3rem 0;
    color: white;
}

.hero h1 {
    font-size: 3rem;
    margin-bottom: 1rem;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

/* Page Grid */
.page-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.page-card {
    background: white;
    padding: 2rem;
    border-radius: 10px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    transition: transform 0.3s, box-shadow 0.3s;
}

.page-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.3);
}

.page-card h3 {
    color: #667eea;
    margin-bottom: 0.5rem;
}

/* Buttons */
.btn {
    display: inline-block;
    padding: 0.75rem 1.5rem;
    background: #667eea;
    color: white;
    text-decoration: none;
    border-radius: 5px;
    border: none;
    cursor: pointer;
    transition: background 0.3s;
    margin: 0.5rem 0.5rem 0.5rem 0;
}

.btn:hover {
    background: #5568d3;
}

.btn-secondary {
    background: #764ba2;
}

.btn-secondary:hover {
    background: #653a8b;
}

/* Info Section */
.info-section {
    background: white;
    padding: 2rem;
    border-radius: 10px;
    margin: 2rem 0;
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}

.info-section h2 {
    color: #667eea;
    margin-bottom: 1rem;
}

.info-section ul {
    margin-left: 2rem;
    margin-top: 1rem;
}

.info-section li {
    margin: 0.5rem 0;
}

/* Page Header */
.page-header {
    text-align: center;
    color: white;
    padding: 2rem 0;
}

.page-header h1 {
    font-size: 2.5rem;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

/* Content Section */
.content-section {
    background: white;
    padding: 2rem;
    border-radius: 10px;
    margin: 2rem 0;
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}

.content-section h2 {
    color: #667eea;
    margin-bottom: 1rem;
}

/* Login Section */
.login-section {
    background: white;
    padding: 2rem;
    border-radius: 10px;
    margin: 2rem 0;
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}

.login-section h2 {
    color: #667eea;
    margin-bottom: 1.5rem;
}

.login-form {
    max-width: 400px;
}

.form-group {
    margin-bottom: 1.5rem;
}

.form-group label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 600;
    color: #333;
}

.form-group input {
    width: 100%;
    padding: 0.75rem;
    border: 2px solid #ddd;
    border-radius: 5px;
    font-size: 1rem;
    transition: border-color 0.3s;
}

.form-group input:focus {
    outline: none;
    border-color: #667eea;
}

/* Navigation Links */
.navigation {
    margin: 2rem 0;
}

/* Footer */
footer {
    text-align: center;
    padding: 2rem;
    color: white;
    margin-top: 3rem;
}

/* Responsive Design */
@media (max-width: 768px) {
    .hero h1 {
        font-size: 2rem;
    }
    
    .page-grid {
        grid-template-columns: 1fr;
    }
    
    .navbar {
        flex-direction: column;
        text-align: center;
    }
    
    .nav-links a {
        margin: 0.5rem;
    }
}
'''
    with open('static/css/style.css', 'w') as f:
        f.write(content)
    print("Created: static/css/style.css")

def create_requirements():
    """Create requirements.txt file"""
    content = '''Flask==3.0.0
Werkzeug==3.0.1
'''
    with open('requirements.txt', 'w') as f:
        f.write(content)
    print("Created: requirements.txt")

def create_readme():
    """Create README.md file"""
    content = '''# Flask Multi-Page Application

A Flask web application with 11 pages, each containing login forms that log submissions.

## Features

- Main index page with navigation to 11 sub-pages
- Individual login forms on each page
- Logging submissions to both terminal and file (submissions.log)
- Responsive design with modern CSS
- Easy navigation between pages

## Setup

1. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://localhost:5000
```

## Project Structure

```
flask-multi-page-app/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── submissions.log         # Login submissions log (created automatically)
├── templates/             # HTML templates
│   ├── base.html          # Base template
│   ├── index.html         # Home page
│   ├── page1.html         # Page 1
│   ├── page2.html         # Page 2
│   └── ...                # Pages 3-11
└── static/                # Static files
    └── css/
        └── style.css      # Stylesheet

```

## Usage

- Navigate to http://localhost:5000 to see the home page
- Click on any page card to visit that page
- Each page has a login form
- Submissions are logged to both terminal and submissions.log file
- Use navigation buttons to move between pages

## Logging

All login submissions are logged with:
- Timestamp
- Page name
- Username
- Password

Logs appear in:
1. Terminal output
2. submissions.log file

## Customization

- Modify templates in the `templates/` directory
- Update styles in `static/css/style.css`
- Add new routes in `app.py`
'''
    with open('README.md', 'w') as f:
        f.write(content)
    print("Created: README.md")

def main():
    """Main setup function"""
    print("=" * 50)
    print("Flask Multi-Page Application Setup")
    print("=" * 50)
    print()
    
    # Create all files and directories
    create_directory_structure()
    create_app_py()
    create_base_template()
    create_index_template()
    create_page_templates()
    create_css()
    create_requirements()
    create_readme()
    
    print()
    print("=" * 50)
    print("Setup Complete!")
    print("=" * 50)
    print()
    print("Next steps:")
    print("1. Create virtual environment: python3 -m venv venv")
    print("2. Activate it: source venv/bin/activate")
    print("3. Install dependencies: pip install -r requirements.txt")
    print("4. Run the app: python app.py")
    print("5. Open browser: http://localhost:5000")
    print()

if __name__ == '__main__':
    main()