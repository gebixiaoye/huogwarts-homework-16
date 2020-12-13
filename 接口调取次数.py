#! /usr/bin/python
#coding=utf-8

from flask import Flask,request
from flask_restful import reqparse,abort,Api,Resource


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('post',type = int )

countNum = []

class postlist(Resource):

    def post(self):
        countNum.append(1)
        result = '此接口调用了{}次'.format(len(countNum))
        print(result)
        return result,201


api.add_resource(postlist,'/posts')

if __name__ == '__main__':
    app.run(debug=True)
