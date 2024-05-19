from flask import Flask, render_template, url_for
import requests
from post import Post

BLOG_ENTRIES_ENDPOINT = 'https://api.npoint.io/d5cf309f34ac12b1c67c'

response = requests.get(BLOG_ENTRIES_ENDPOINT)
all_posts_data = response.json()

all_posts = []
for post in all_posts_data:
    post_entry = Post(id=post["id"],
                      title=post["title"],
                      subtitle=post["subtitle"],
                      body=post["body"],
                      image_url=post["image_url"],
                      date=post["date"],
                      author=post["author"])
    all_posts.append(post_entry)

app = Flask(__name__)


@app.route("/")
def get_all_posts():
    return render_template("index.html", posts=all_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route('/post/<int:num>')
def get_post(num):
    return render_template("post.html", posts=all_posts, id=num)


if __name__ == "__main__":
    app.run(debug=True)