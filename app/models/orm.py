from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
        __tablename__  = 'students'
        email = db.Column(db.String(60), primary_key=True,unique=True, nullable=False)
        student_name = db.Column(db.String(120), nullable=False)
        phone = db.Column(db.String(15), nullable=False)    
        cell =  db.Column(db.String(150), nullable=False)
        def __repr__(self):
                return '<Student %r>' % self.student_name
        
        def __init__(self, email, student_name, phone, cell):
                self.email = email
                self.student_name = student_name
                self.phone = phone
                self.cell = cell

class Class(db.Model):
        __tablename__  = 'classes'
        id = db.Column(db.Integer, primary_key=True,)
        date = db.Column(db.DateTime, nullable=False)
        student_id = db.Column(db.String(60), db.ForeignKey('students.email'),
        nullable=False)
        student = db.relationship('Student',
                backref=db.backref('students', lazy=True))


        