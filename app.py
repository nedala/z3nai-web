from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/favicon.ico")
def favicon():
	return app.send_static_file("dist/images/favicon.ico")

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=10000, debug=True)