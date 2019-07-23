from flask import Flask, render_template, request, send_from_directory, jsonify

web = Flask(__name__)

@web.route("/")
def index():
    return render_template("login.html")


@web.route('/assets/<path:path>')
def send_js(path):
    return send_from_directory('templates/assets/', path)

if __name__ == "__main__":
    web.run(debug=True, port=5001)

