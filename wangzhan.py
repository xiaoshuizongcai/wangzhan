from flask import Flask
app=Flask(__name__)
@app.route("/")#制作网站
def index():
    return "<h1>网站设计中，请稍等</h1><h2>hello</h2><h3>hello<h3><img src='http://www.css5.com.cn/uploads/20200521020122.jpg' />"#网站上的文字(h1大标题，h2中标题，数字越大字越小)
@app.route("/he")
def he():
    return"<h1>hello</h1>"#在这个网站里进入另一个位置（如翻页、链接）