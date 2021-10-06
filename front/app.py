from flask import Flask

app=Flask("mana_alle")

@app.route("/")
def index():
    return "<h1>このページはいつも通りゴミページです。</h1>"

@app.errorhandler(404)
def not_found(error):
    return "<h1>ばーか、ばーか。そんなページあると思ったか!</h1><image src='https://c.tenor.com/A6KL5abo-_AAAAAM/wreck-it-ralph2-vanellope.gif'></image>"