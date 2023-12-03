# app.py
from flask import Flask, render_template, request, redirect, url_for, session
from datetime import timedelta
app = Flask(__name__)

app.secret_key = 'your_secret_key'  # Change this to a secret key for your application
app.permanent_session_lifetime = timedelta(minutes=20)

# Mock user data (for demonstration purposes)
users = {'user1': 'password1', 'user2': 'password2'}

#@app.route('/')
#def index():
#    if 'username' in session:
#        return 'Logged in as ' + session['username'] + '<br>' + \
#               "<b><a href = '/logout'>click here to log out</a></b>"
#    return "You are not logged in <br><a href = '/login'></b>" + \
#           "click here to log in</b></a>"

@app.route('/')
def index():
    if 'username' in session:
        data = {
            'username': session['username'],
            'message': 'Welcome back!',
            'logout_url': url_for('logout')
        }
        return render_template('index.html', data=data)
    return render_template('index.html', data=None)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('index'))
        return 'Invalid login'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

#@app.route('/', methods=['GET', 'POST'])
#def home():
#    message = "hello world"
#    return render_template('home.html',message=message)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Здесь можно добавить код для обработки введенных данных (регистрации пользователя)
        
        return 'Регистрация успешно завершена!'
    
    return render_template('register.html')

if __name__ == '__main__':
    app.run()

@app.route('/')
def hello_world():
   return 'Hello World'

if __name__ == '__main__':
   app.run()
