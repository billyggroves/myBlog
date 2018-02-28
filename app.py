import os
from flask_sqlalchemy import SQLAlchemy
from flask_jsglue import JSGlue
from flask import Flask, render_template, request, session, jsonify
from sqlalchemy import desc
from datetime import datetime
from blogPost import BlogPost

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = ''
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# class Blog(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     imgHead = db.Column(db.String(80), unique=False, nullable=True)
#     title = db.Column(db.String(80), unique=True, nullable=False)
#     subtitle1 = db.Column(db.String(80), unique=False, nullable=True)
#     intro = db.Column(db.Text, unique=True, nullable=False)
#     subtitle2 = db.Column(db.String(80), unique=False, nullable=True)
#     body = db.Column(db.Text, unique=True, nullable=True)
#     subtitle3 = db.Column(db.String(80), unique=False, nullable=True)
#     conclusion = db.Column(db.Text, unique=True, nullable=True)
#     date = db.Column(db.DateTime, unique=True, nullable=False)

#     def __init__(self, id, imgHead, title, subtitle1, intro, subtitle2, body, subtitle3, conclusion, date):
#         self.id = id
#         self.imgHead = imgHead
#         self.title = title
#         self.subtitle1 = subtitle1
#         self.intro = intro
#         self.subtitle2 = subtitle2
#         self.body = body
#         self.subtitle3 = subtitle3
#         self.conclusion = conclusion
#         self.date = date


JSGlue(app)


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post", methods=['GET', 'POST'])
def post():
    if request.method == "GET":

        posts = Blog.query.order_by(desc(Blog.date)).first()
        post = BlogPost(1, posts.imgHead, posts.title, posts.subtitle1, posts.intro, posts.subtitle2, posts.body, posts.subtitle3, posts.conclusion, posts.date)


        return render_template("post.html", blogPost=post)

    else:    
        return render_template("/about")

@app.route("/admin", methods=['GET', 'POST'])
def admin():
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return render_template("adminLogin.html")

        # Ensure password was submitted
        if not request.form.get("password"):
            return render_template("adminLogin.html")

        print("TEST!!!!!!")
        print(request.form.get("username"))
        print(request.form.get("password"))
        

        if request.form.get("username") == "" and request.form.get("password") == "":
            return render_template("insertBlog.html")
        
        return render_template("adminLogin.html")

    else:
        return render_template("adminLogin.html")

@app.route("/_insertBlog", methods=['GET', 'POST'])
def _insertBlog():
    if request.method == "POST":
        # Server-side validation
        if not request.form.get("title"):
            return render_template("insertBlog.html")

        if not request.form.get("introduction"):
            return render_template("insertBlog.html")

        # Variable initialization
        img = "/static/img/"
        img += "personal background.jpg"
        blogTitle = request.form.get("title")
        blogSub1 = request.form.get("subtitle1")
        blogIntro = request.form.get("introduction")
        blogSub2 = request.form.get("subtitle2")
        blogBody = request.form.get("body")
        blogSub3 = request.form.get("subtitle3")
        blogConclusion = request.form.get("conclusion")
        blogTime = datetime.now()

        #Insert new Blog
        newBlog = Blog(None, img, blogTitle, blogSub1, blogIntro, blogSub2, blogBody, blogSub3, blogConclusion, blogTime)
        db.session.add(newBlog)
        db.session.commit()


        return jsonify(result="Success!!!")

    else:
        return render_template("adminLogin.html")