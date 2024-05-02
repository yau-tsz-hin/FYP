#  這是應用程序包的初始化文件，Flask將從這裡開始運行。
#  這個文件的作用是初始化Flask應用程序，並將路由和錯誤處理程序連接到應用程序。


from flask import Flask, render_template, request, redirect, abort, send_file, url_for
import os

from pathlib import Path

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    id = request.form.get('id')
    
    if id == "buy_gbl":
        return redirect('https://youtu.be/UIp6_0kct_U')
    
    elif id == "download_mc_mod":
        return render_template('download_mod.html')
    
    elif id == "dlmcmodac":
        return render_template('home.html')
                
    else:
        return abort(400, "Invalid id: {}".format(id))



# 你必須保持路由定義在最後。


from app import routes, errors
