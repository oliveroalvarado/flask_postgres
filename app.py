from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://oliveralvarado@localhost/students'
db = SQLAlchemy(app)

# referencing the student table in my db as a Model
class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(1))

# creating a route to, using a GET method
@app.route('/api/v1/old_students', methods=['GET'])
def get_old_students():
    # created variable to append to for students base on age
    old_students = []
    # made a variable that takes all the students from "student" db in my local system
    students = Students.query.all()
    # converted students var in to a JSON 
    json_students = [{'id':stud.id, 'first_name':stud.first_name, 'last_name':stud.last_name, 'age':stud.age, 'grade':stud.grade} for stud in students]
    #iterate through the json_student and append all that meets contiditional statement 
    for stud in json_students:
        if stud['age'] >= 20:
            old_students.append(stud)
    return jsonify(old_students)


@app.route('/api/v1/young_students', methods=['GET'])
def get_young_students(): 
    young_students = []
    students = Students.query.all()
    json_students = [{'id':stud.id, 'first_name':stud.first_name, 'last_name':stud.last_name, 'age':stud.age, 'grade':stud.grade} for stud in students]
    for stud in json_students:
        if stud['age'] < 21:
            young_students.append(stud)
    return jsonify(young_students)

@app.route('/api/v1/advance_students', methods=['GET'])
def get_advance_students(): 
    advance_students = []
    students = Students.query.all()
    json_students = [{'id':stud.id, 'first_name':stud.first_name, 'last_name':stud.last_name, 'age':stud.age, 'grade':stud.grade} for stud in students]
    for stud in json_students:
        if stud['age'] < 21 and stud['grade'] == 'A':
            advance_students.append(stud)
    return jsonify(advance_students)

@app.route('/api/v1/name_students', methods=['GET'])
def get_name_students(): 
    students = Students.query.all()
    json_names_students = [{'first_name':stud.first_name, 'last_name':stud.last_name} for stud in students]
    return jsonify(json_names_students)

@app.route('/api/v1/students', methods=['GET'])
def get_students(): 
    students = Students.query.all()
    json_students = [{'id':stud.id, 'first_name':stud.first_name, 'last_name':stud.last_name, 'age':stud.age, 'grade':stud.grade} for stud in students]
    return jsonify(json_students)

if __name__== '__main__':
    app.run(debug=True)