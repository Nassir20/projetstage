from flask import Flask, render_template
import datetime
app= Flask(__name__)

@app.route("/")
def webapp():
    return render_template("index.html")
@app.route("/heure")
def date():
    date_heure = datetime.datetime.now()
    h = date_heure.hour
    m = date_heure.minute
    s = date_heure.second
    return render_template("h.html", heure=h,min=m,sec=s)
@app.route("/formulaire")
def form():
    return render_template("formulaire.html")
if __name__== '__main__':
    app.run(debug=True)