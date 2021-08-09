import flask as Flask


try:
    import sys
except ImportError:
    print('sys : Module not found.  ')
try:
    import os
except ImportError:
    print('os : Module not found')
try:
    from flask import *
except ImportError:
    print('flask : Module not found')

try:
    import json
except ImportError:
    print('  json : library not found.  ')
    print('flask : Module not found')

from helpers import utils

data = []
app = Flask(__name__)
app.secret_key = 'Let it be a secrete'


@app.route("/5", methods=['GET', 'POST'])
def five_solution():
    asset_metadata=[]
   # response = utils.getAccessToken(2)
 
    return render_template('5.html')

@app.route("/ingest", methods=['GET', 'POST'])
def ingest():
    file_name = request.form.popitem()
    asset_url = request.args.get('url')
    asset_metadata=[]
   # response = utils.getAccessToken(2)
    print(file_name )
    return jsonify("{'status' : 'ok'}")


@app.route("/2", methods=['GET', 'POST'])
def two_solution():
    asset_metadata=[]
    response = utils.getAccessToken(1)
    asset_details = utils.get_videos(response)
    
    for asset in asset_details:
        asset_metadata.append([asset['id'] , asset['name']])
    print(asset_metadata)
    return render_template('2.html',data=asset_metadata, act=response)

@app.route("/1", methods=['GET', 'POST'])
def one_solution():

    return render_template('1.html')

@app.route("/3", methods=['GET', 'POST'])
def three_solution():

    return render_template('3.html')

@app.route("/", methods=['GET', 'POST'])
def index():

    return render_template('3.html')

if __name__ == '__main__':
    app.run(debug=True)
