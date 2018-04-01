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
        return redirect(url_for("page_not_found", "error"))


@app.route("/blog/<blogTitle>", methods=['GET', 'POST'])
def blog(blogTitle):
    if request.method == "GET":
        if blogTitle == "":
            return redirect(url_for("page_not_found", "error"))

        if blogTitle == None:
            return redirect(url_for("page_not_found", "error"))

        name = blogTitle + ".html"
        print(name)
        # CITATION: https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory
        for filename in os.listdir("./templates/blogPosts"):
            print(filename)
            if filename.lower() == name:
                post = "blogPosts/" + name
                print(post)
                return render_template(post)

        return redirect(url_for("page_not_found", "error"))
    
    else:
        return redirect(url_for("page_not_found", "error"))
    
    return redirect(url_for("page_not_found", "error"))


# CITATION: http://flask.pocoo.org/docs/0.12/patterns/errorpages/
@app.errorhandler(404)
@app.route("/page_not_found")
def page_not_found(e):
    return render_template('404.html'), 404