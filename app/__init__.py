#  這是應用程序包的初始化文件，Flask將從這裡開始運行。
#  這個文件的作用是初始化Flask應用程序，並將路由和錯誤處理程序連接到應用程序。
from app import DB

from flask import Flask, render_template, request, redirect, abort, send_file, url_for, flash, session
import os

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash

from pathlib import Path

app = Flask(__name__)

logined = False

@app.route("/login", methods=['POST'])
def login():
    global logined
    user_info = request.get_json(force=True)
    print(user_info)
    user_username = user_info["email"]
    print(user_username)
    user_password = user_info["password"]
    print(user_password)
    DB.cursor.execute(f"SELECT users.\"Password\" FROM users WHERE users.\"Username\" = '{user_username}' OR users.\"Email\" = '{user_username}'")
    correct_password = DB.cursor.fetchone()
    print(correct_password)
    return_val = ""
    try:
        correct_password = correct_password[0]
        if(correct_password == user_password):
            logined = True
            print(logined)
            return_val = "Success"
        elif(correct_password == None):
            return_val = "Failed"
        else:
            return_val = "Failed"
    except:
        print(f"Error: {correct_password}")
        return_val = "Failed"
    return f'{return_val}'

@app.route("/logindone")
def logindone():
    if(logined == True):
        print(logined)
        return render_template("loginhome.html")
    else:
        return "failed to login"



@app.route('/')
@app.route('/index.html')
def home():
    global logined
    logined = False
    print(logined)
    return render_template('index.html')

#render_template about.html
@app.route('/about.html')
def about():
    global logined
    logined = False
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    global logined
    logined = False
    return render_template('contact.html')

@app.route('/service.html')
def service():
    global logined
    logined = False
    return render_template('service.html')

@app.route('/typography.html')
def typography():
    global logined
    logined = False
    return render_template('typography.html')

@app.route('/gallery.html')
def gallery():
    global logined
    logined = False
    return render_template('gallery.html')



# 你必須保持路由定義在最後。


from app import routes, errors
