#SETUP / BACKGROUND
#import / configure flask and sqlalchemy elements, link up to database
from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import flask_sqlalchemy

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


if __name__ == "__main__":
    app.run()