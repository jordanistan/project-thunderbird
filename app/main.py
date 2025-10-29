from flask import Flask, render_template, request, session, redirect, url_for
import json
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Create a serializer object
s = URLSafeTimedSerializer(app.secret_key)

@app.route('/')
def index():
    if 'email' in session:
        return redirect(url_for('authenticated'))
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/auth', methods=['POST'])
def auth():
    email = request.form['email']
    with open('/usr/src/app/config/authorized_emails.json') as f:
        authorized_emails = json.load(f)['authorized_emails']
    
    if email in authorized_emails:
        # Generate a token
        token = s.dumps(email, salt='email-confirm')
        
        # Create the verification link
        link = url_for('verify_email', token=token, _external=True)
        
        # For now, just print the email to the console
        print(f'Click this link to verify your email: {link}', flush=True)
        
        return "Please check your email for a verification link."
    else:
        return "Sorry, your email is not authorized."

@app.route('/verify_email/<token>')
def verify_email(token):
    try:
        email = s.loads(token, salt='email-confirm', max_age=3600)
        session['email'] = email
        return redirect(url_for('authenticated'))
    except SignatureExpired:
        return '<h1>The token is expired!</h1>'
    except Exception as e:
        return f'<h1>An error occurred: {e}</h1>'

@app.route('/authenticated')
def authenticated():
    if 'email' in session:
        master_password = "your-1password-master-password"
        return render_template('authenticated.html', master_password=master_password)
    return redirect(url_for('login'))

@app.route('/unlock', methods=['POST'])
def unlock():
    if 'email' not in session:
        return redirect(url_for('login'))
    
    key = request.form['key']
    # For now, just print the key to the console
    print(f"Encrypted key: {key}")
    
    # TODO: Decrypt the key and unlock the media folder
    
    return "Unlock functionality is not yet implemented."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
