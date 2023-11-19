from flask import Flask, request, render_template
import requests

app = Flask(__name__)
 
@app.route('/', methods =["GET", "POST"])
def index():
  return render_template("hello world")
    '''weatherData = ''
    error = 0
    cityName = ''
    if request.method == "POST":      
        cityName = request.form.get("cityname")  
        if cityName:
            weatherApiKey = 'Your API Key Goes Here'
            url = "https://api.openweathermap.org/data/2.5/weather?q="+cityName+"&appid=" + weatherApiKey
            weatherData = requests.get(url).json()
        else:
            error = 1    
    return render_template('index.html', data = weatherData, cityName = cityName)'''
if __name__ == "__main__":
    app.run()
