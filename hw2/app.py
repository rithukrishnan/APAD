from operator import methodcaller
import os
import time
from flask import Flask, send_from_directory
import json



app = Flask(__name__, static_folder='build', static_url_path='/')

#This route gets called and argument name is passed.
@app.route('/api/getter/<name>', methods=['GET'])
def getter_api(name):
    print(name)
    if name == "Rithu" or name == "rithu":
        #Process the output and send a json
        return {"output": "Anand Krishnan"}
    else:
        return  {"output": "User not found!"}
    


@app.route('/', methods=['GET'])
def index():
    return send_from_directory(app.static_folder, 'index.html')

   
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=80)

@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')