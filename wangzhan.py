from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")#制作网站
def index():
    return render_template('index.html')
@app.route("/he/<name>")
def he(name):
    return render_template('he.html',name=name)#在这个网站里进入另一个位置（如翻页、链接）