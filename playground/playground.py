from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def whoopsie():
	return redirect("http://localhost:5000/play")

@app.route('/play')
def index():
	return render_template("index.html", times=3)

@app.route('/play/<times>')
def times(times):
	return render_template("index.html", times=int(times))

@app.route('/play/<times>/<color>')
def color(times, color):
	return render_template("index.html", times=int(times), color= color)

if __name__=="__main__":
	app.run(debug=True)