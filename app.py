from flask import Flask

app=Flask(__name__)
@app.route('/')
def welcome():
  return "<h1>Hello, welcome to flask app1 </h1>"
@app.route('/user')
def user():
  return "<h2>Hello,This is user page </h2>"
# from controller import product_control,user_control
from controller import *
