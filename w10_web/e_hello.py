# popis:
# https://www.tutorialspoint.com/flask/flask_application.htm
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_flask():
   return 'Toto je Flask'

# Mapování metod na URL 
@app.route('/hello')
def hello_world():
   return 'hello world'

# lze to i takto:
# def hello_world():
#   return 'hello world'
# app.add_url_rule('/', 'hello', hello_world)

# dynamické URL:
@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

# lze zadat i typ:
# int,
# float, 
# path   - str včetně lomítek 
@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

# přesměrování pomocí redirect a url_for:
from flask import redirect, url_for
@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_world'))
   else:
      return redirect(url_for('hello_name',name = name))

if __name__ == '__main__':
   app.run()
   #app.run(host='127.0.0.1', port=5000, debug=False, options)