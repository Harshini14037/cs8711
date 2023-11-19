from flask import Flask, request, render_template
import requests

app = Flask(__name__)
 
@app.route('/', methods =["GET", "POST"])
def index():
  return render_template("hello world")
    
if __name__ == "__main__":
    app.run()
