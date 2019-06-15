from flask_restful import Resource, Api
from flask import jsonify,request
class RegisterUser(Resource):

    def post(self):
        try:    
            data = {}
            schema = ['email', 'name', 'phone', 'cell']
            for field in schema:
                try:
                    data[field] = request.form[field]
                except Exception as error:
                    error[field]="Not validated"
            return {"result":"user registered"}
        except Exception as error:
            return {"result":"Error: {}".format(error)}
