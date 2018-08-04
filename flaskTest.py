from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return str(open("response.txt").read().strip())

@app.route("/play")
def main():
    return render_template("index.html")

if __name__ == '__main__':
	app.run(port="9000")