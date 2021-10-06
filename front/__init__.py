from flask import Flask, render_template

app=Flask(__name__)
print(app.template_folder)
@app.route("/")
def index():
    return render_template("index.html")

@app.errorhandler(404)
def not_found(error):
    return "<h1>ばーか、ばーか。そんなページあると思ったか!</h1><image src='https://c.tenor.com/A6KL5abo-_AAAAAM/wreck-it-ralph2-vanellope.gif'></image>"