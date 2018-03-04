#!flask/bin/python
import json
from flask import Flask, Response
from helloworld.flaskrun import flaskrun

application = Flask(__name__)

@application.route('/', methods=['GET'])
def get():
    #return "You used get!"
    return Response(json.dumps({'Output': 'FOO BAR!!!'}), mimetype='application/json', status=200)

@application.route('/', methods=['POST'])
def post():
    #return "You used post!"
    return Response(json.dumps({'Output': 'ABC'}), mimetype='application/json', status=200)

if __name__ == '__main__':
    flaskrun(application)
