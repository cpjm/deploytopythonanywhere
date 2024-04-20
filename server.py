# setyp virtual environment
# anaconda command prompt
# python -m venv venv
# .\venv\Scripts\activate.bat
# pip install flask
# python server.py
#  -> reports Running on http://127.0.0.1:5000
#   -> browse to http://127.0.0.1:5000
# 
# 
# 

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"
    firt 
if __name__ == "__main__":
    app.run(debug = True)