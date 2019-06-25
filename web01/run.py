from flask import Flask, render_template, request, send_from_directory, url_for, redirect

app = Flask(__name__)


@app.route("/")
def root():
    return render_template("login.html")

@app.route('/assets/<path:path>')
def send_js(path):
    return send_from_directory('templates/assets/', path)


if __name__ == "__main__":
    app.run(debug=True)
