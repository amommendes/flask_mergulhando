from flask_restful import Resource, Api
from flask import jsonify,request
from app.models.orm import Student, Class
from app.models.orm import db 
from app.utils.authentication_sheets import AuthenticationSheets
import datetime

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
                spreadsheets.values().append(spreadsheetId="1zcfjKED57IuFm9nbX67GdNgp3fXWggxDyWOdhTagyiY",
                    range="Alunos!A:D",
                    valueInputOption="USER_ENTERED",
                    body=body
                ).execute()
                db.session.commit()
                return {"result":"success"}
            except Exception as error:
                return {"result":"failed: {} / {}".format(error, body)}
        else:
            return {"result":"duplicated"}

class RegisterPresence(Resource):
    def post(self):
        email = request.form["email"]
        date = datetime.date.today()
        authenticator = AuthenticationSheets()
        spreadsheets = authenticator.get_service
        has_presence = True if Class.query.filter_by(student_id=email, date=date).first() else False
        student = Student.query.filter_by(email=request.form["email"]).first()
        if has_presence and student:
            return {"result":"duplicated"}
        elif not student:
            return {"result":"user not found"}
        else:
            try:
                record = Class(date,email)
                student.students.append(record)
                db.session.add(student)
                row = [date.strftime("%Y-%m-%d"),email]
                body = { 'values': [row] }
                spreadsheets.values().append(spreadsheetId="1zcfjKED57IuFm9nbX67GdNgp3fXWggxDyWOdhTagyiY",
                    range="Presenças!A:B",
                    valueInputOption="USER_ENTERED",
                    body=body
                ).execute()
                db.session.commit()
                return {"result":"success"}
            except Exception as error:
                return {"result":"{}".format(error)}

                