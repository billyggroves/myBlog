import os
from flask_jsglue import JSGlue
from flask import Flask, render_template, request, url_for, redirect
from datetime import datetime
from blogPost import BlogPost

app = Flask(__name__)
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
        return render_template("allPosts.html")
    
    else:
        return redirect(url_for("page_not_found"))


@app.route("/blog/<blogTitle>", methods=['GET', 'POST'])
def blog(blogTitle):
    if request.method == "GET":
        if blogTitle == "":
            return redirect(url_for("page_not_found"))

        if blogTitle == None:
            return redirect(url_for("page_not_found"))

        name = blogTitle + ".html"
        # CITATION: https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory
        for filename in os.listdir("./templates/blogPosts"):
            if filename.lower() == name:
                post = "blogPosts/" + name
                return render_template(post)

        return redirect(url_for("page_not_found"))
    
    else:
        return redirect(url_for("page_not_found"))
    
    return redirect(url_for("page_not_found"))


# CITATION: http://flask.pocoo.org/docs/0.12/patterns/errorpages/
@app.errorhandler(404)
@app.route("/page_not_found", methods=['GET', 'POST'])
def page_not_found(e):
    return render_template('404.html'), 404