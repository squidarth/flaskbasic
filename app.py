from flask import Flask, render_template, jsonify, request
from database import db_session
import requests
from models import BlogPost

app = Flask(__name__)
app.config["DEBUG"] = True

@app.teardown_appcontext
def shutdown_session(exception=None):
      db_session.remove()

@app.route("/posts")
def posts():
  blog_posts = BlogPost.query.all()
  return render_template("posts.html", posts=blog_posts)

@app.route("/post/<post_id>")
def post(post_id):
  blog_post = BlogPost.query.filter_by(id=post_id).first()
  return render_template("post.html", post=blog_post)

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

@app.route("/create-post", methods=["POST"])
def create_post():
  post = BlogPost(title=request.form["title"], 
                  content=request.form["content"])
  db_session.add(post)
  db_session.commit()
  print(request.form["title"])
  print(request.form["content"])
  return "Was successful"

if __name__ == "__main__":
      app.run(host="0.0.0.0")
