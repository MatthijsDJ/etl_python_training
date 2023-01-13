from flask import (Flask,
                   request,
                   render_template)

app = Flask(__name__)

@app.route("/")
def hello_word():
    return render_template('index.html', data={})


@app.route('/etl/jobs')
def show_etl_jobs():
    return "<h1>ETL</h1>"


@app.route('/etl/jobs/<string:name>')
def show_etl_jobs_details(name):
    return f"<h1>ETL {name}</h1>"