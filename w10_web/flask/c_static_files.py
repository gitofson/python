# Pokud potřebujeme statickjé soubory, např. .css, či .js, dáme je do složky ./static
# a odkážeme se na ně např. html template  pomocí 
# src = "{{ url_for('static', filename = 'c_hello.js') }}"
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
   return render_template("c_index.html")

if __name__ == '__main__':
   app.run(debug = True)