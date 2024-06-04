from flask import Flask, render_template, request, session, redirect, url_for  

app = Flask(__name__)  
app.secret_key = 'secret-key'  # This should be a long, random string

# Mock user database
users = {  
    'som': 'password',  
    'jane': 'password'  
}  

# Login route
@app.route('/login', methods=['GET', 'POST'])  
def login():  
    if request.method == 'POST':  
        username = request.form['username']  
        password = request.form['password']  
        if username in users and users[username] == password:  
            session['username'] = username  
            return redirect(url_for('dashboard'))  
        else:  
            return render_template('login.html', error='Invalid username or password')  
    else:  
        return render_template('login.html')  

# Dashboard route
@app.route('/dashboard')  
def dashboard():  
    if 'username' in session:  
        username = session['username']  
        return render_template('dashboard.html', username=username)  
    else:  
        return redirect(url_for('login'))  

# Logout route
@app.route('/logout')  
def logout():  
    session.pop('username', None)  
    return redirect(url_for('login'))  

if __name__ == '__main__':  
    app.run(debug=True)
