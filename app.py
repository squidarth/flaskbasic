from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def hello():
      return render_template("hello.html")

@app.route("/name")
def name():
  return "Sid"

@app.route("/search/<search_query>")
def search(search_query):
    return search_query

@app.route("/add/<x>/<y>")
def add(x,y):
  return str(int(x) + int(y))

@app.route("/search_github/<search_query>")
def search_github(query):
  url = "https://api.github.com/search/repositories?q=" + search_query
  response_dict = requests.get(url).json()
  return response_dict["total_count"]

if __name__ == "__main__":
      app.run(host="0.0.0.0")
