from flask_restful import Resource, Api
from flask import jsonify,request
from app.models.orm import Student
from app.models.orm import db 
from app.utils.authentication_sheets import AuthenticationSheets


class RegisterUser(Resource):
    def post(self):
        student_exists = True if Student.query.filter_by(email=request.form["email"]).first() else False
        authenticator = AuthenticationSheets()
        spreadsheets = authenticator.get_service
        if (not student_exists):
            data = {}
            errors = {}    
            try:    
                schema = ['email', 'name', 'phone', 'cell']
                for field in schema:
                    try:
                        data[field] = request.form[field]
                    except Exception as error:
                        errors[field]="Not validated"
                record = Student(data["email"], data["name"], data["phone"], data["cell"])
                db.session.add(record)
                row = [data[key] for key in data]
                body = { 'values': [row] }
                db.session.commit()
                spreadsheets.values().append(spreadsheetId="1zcfjKED57IuFm9nbX67GdNgp3fXWggxDyWOdhTagyiY",
                    range="Alunos!A:D",
                    valueInputOption="USER_ENTERED",
                    body=body
                ).execute()
                return {"result":"success"}
            except Exception as error:
                return {"result":"failed: {} / {}".format(error, body)}
        else:
            return {"result":"duplicated"}
    