from flask import Flask
from flask import request
from flask import render_template
import csv
import datetime


app = Flask(__name__, static_url_path="/static")


@app.route('/', methods=['POST','GET'])
def index():
    if request.method == "POST":
        confession = request.form['confession']
        with open("confessions.csv","a") as f:
            csvw = csv.writer(f)
            dateAndTime= datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            csvw.writerow([dateAndTime,confession])
        return render_template("thanks.html")
    return render_template("index.html")

@app.route('/confessions', methods=['GET', 'POST'])
def confessions():
    with open("confessions.csv","r") as f:
        csvr = csv.reader(f)
        l = []
        for a in csvr:
            if a:
                date_time = datetime.datetime.strptime(a[0], "%Y-%m-%d %H:%M:%S")
                date = date_time.strftime("%d %B %Y")
                time = date_time.strftime("%I:%M:%S %p")
                l.append([date,time,a[1]])
        l.reverse()
    return render_template('confessions.html',confessions=l)

if __name__ == "__main__":
    app.run(debug=True, port="5500")