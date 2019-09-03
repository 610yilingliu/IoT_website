from app import app
from flask import render_template, request, flash, redirect, session, url_for ,logging
# hard-coded user info
from app.users import userinfo

@app.route('/',methods=['GET', 'POST'])
def login():
    user_info = userinfo()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        is_exist = False
        for item in user_info:
            if item['username'] == username:
                is_exist = True
                is_correct = (item['password'] == password)
                if is_correct == True:
                    session["logged_in"]=True
                    return redirect(url_for('index'))
                else:
                    flash('Incorrect password','warning')
        if is_exist == False:
            flash('User not exist','warning')
    return render_template('login.html')

@app.route('/index')
def index():
    if session["logged_in"]:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))
