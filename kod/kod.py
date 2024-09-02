from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  

users = {
    "test@example.com": "password123"  
}

@app.route('/', methods=['GET', 'POST'])
def home():
    success_message = None
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        users[email] = password  
        success_message = "Başarıyla kayıt oldunuz!"
    return render_template('index.html', success_message=success_message)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error_message = None
    if request.method == 'POST':
        email = request.form.get('email').strip()  
        password = request.form.get('password').strip() 
        if email in users and users[email] == password:
            return redirect(url_for('welcome'))
        else:
            error_message = "Yanlış e-posta veya şifre"
    return render_template('login.html', error_message=error_message)

@app.route('/welcome')
def welcome():
    return "Giriş başarılı! Hoş geldiniz."

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
