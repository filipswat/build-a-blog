#SETUP / BACKGROUND
#import / configure flask and sqlalchemy elements, link up to database
from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://build-a-blog:password@localhost:8889/build-a-blog"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

#create class for blog posts (5000 char limit on content set to approx 1000 words)
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    content = db.Column(db.String(6000))

    def __init__(self, title, content):
        self.title = title
        self.content = content


#APP ROUTES / HANDLERS
#root directory just redirects to main blog page
@app.route("/")
def redirector():
    return redirect("/blog")

@app.route("/blog", methods=["POST", "GET"])
def index():     
    if request.method == "POST":
        new_title = request.form["title"]
        new_content = request.form["content"]
        new_post = BlogPost(new_title, new_content)
        db.session.add(new_post)
        db.session.commit()
    
    view_post_id = request.args.get("post_id")
    if view_post_id:
        view_post = BlogPost.query.get(int(view_post_id))
    else:
        view_post = ""
    
    posts = BlogPost.query.filter_by().all()

    return render_template("blog.html", posts=posts, view_post=view_post)

@app.route("/add-post", methods=["GET"])
def add_post():
    return render_template("add-post.html")

#only run when supposed to
if __name__ == "__main__":
    app.run()