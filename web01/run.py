from flask import Flask, render_template, request, send_from_directory, jsonify
from flask import session
import routeros_api
import pandas as pd 

app = Flask(__name__)


@app.route("/")
def root():
    session['logedin']=False 
    return render_template("index.html", pesan_error = "")

@app.route('/assets/<path:path>')
def send_js(path):
    return send_from_directory('templates/assets/', path)

@app.route("/login", methods=["GET"])
def login():
    session['logedin']=False
    if 'username' in request.args and 'password' in request.args:
        #ambil data username dan password yang dikirim oleh browser
        username = request.args['username']    
        password = request.args['password']    
        #persiapkan koneksi ke router
        koneksi = routeros_api.RouterOsApiPool('192.168.1.100', 
                  username=username, password=password)
        try:
            #proses login ke router
            api = koneksi.get_api()
            output = {'state': True, 'message': 'Login berhasil'}
            session['logedin']=True
            session['username']= username 
            session['password']= password
        except:
            output = {'state': False, 'message': 'Login gagal! Username/password salah'}
    else:
        output = {'state': False, 'message': 'Username/password belum lengkap'}
    return jsonify(output)
        
@app.route("/home")
def home():
    if session['logedin']==True:
        koneksi = routeros_api.RouterOsApiPool('192.168.1.100', 
                  username=session['username'], password=session['password'])
        api = koneksi.get_api()
        #ambil data user yang ada di router
        ip = api.get_resource("/ip/address").get()
        return render_template("home.html", data = ip)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.secret_key='abj'
    app.run(debug=True)
