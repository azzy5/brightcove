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



data = []
app = Flask(__name__)
app.secret_key = 'Let it be a secrete'


@app.route("/", methods=['GET', 'POST'])
def index():

    return render_template('2.html')

if __name__ == '__main__':
    app.run(debug=False)
