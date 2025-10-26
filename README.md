# Flask Multi-Page Application

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
source venv/bin/activate  # On Windows: venv\Scripts\activate
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
