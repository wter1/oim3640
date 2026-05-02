from flask import Flask, render_template

app = Flask(__name__) #Object oriented?

@app.route('/') #Simple "/" is just the "root"
def home():
    return "Hello, Babson! Let's build some web applications"

@app.route("/hello")
@app.route('/hello/<name>')
def hello(name=None):
    if name is None:
        name = "Babson"
    name = name.capitalize()
    return render_template("hello.html", name = name)#h1 means first level heading and p means paragraph

@app.route('/square/<int:number>')
def square(number):
    result = number ** 2
    return render_template("square.html", number=number, square=result)



#TODO: Create another route that shows the current price of any stock or current temperature of any city
#/weather/<city>
#/stock/<ticker>

from stocks import get_price

@app.route("/stock/<ticker>")
def stock(ticker):
    price = get_price(ticker)
    return f"The current price of {ticker.upper()} is ${price: .2f}. "

# from weather import get_weather
# @app.route("/weather/<city>")
# def weather(city):
#     weather = get_weather(city)
#     return f"The current weather in {city} is {weather}°F"

if __name__ == '__main__': #Wrap all test code into here so it won't run when the file is ran
    app.run(debug=True)