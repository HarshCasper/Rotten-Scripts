from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/tutorial"
db = SQLAlchemy(app)


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(20), nullable = False)
    join_date = db.Column(db.DateTime)

    courses = db.relationship('Course', secondary='user_course', backref='member', lazy='dynamic')


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))


db.Table('user_course',
         db.Column('member_id', db.Integer, db.ForeignKey('member.id')),
         db.Column('course_id', db.Integer, db.ForeignKey('course.id'))
         )


# db.create_all()

# adding some values in course table
'''
course1 = Course(name='Python')
course2 = Course(name='SQL')
course3 = Course(name='Pornography')
db.session.add(course1)
db.session.add(course2)
db.session.add(course3)
db.session.commit()
'''

course1 = Course.query.filter(Course.name == 'Python').first()
course2 = Course.query.filter(Course.name == 'SQL').first()
print('This displays the list of members having {} : '.format(course1.name), course1.member)
print('This displays the list of members having {} : '.format(course2.name), course2.member)


# fetching and then adding some members in course
# fetching :
mem_1 = Member.query.filter(Member.id == 1).first()
mem_2 = Member.query.filter(Member.id == 4).first()
mem_3 = Member.query.filter(Member.id == 5).first()
mem_4 = Member.query.filter(Member.id == 6).first()
# adding :
course1.member.append(mem_1)
course2.member.append(mem_2)
course1.member.append(mem_3)
course2.member.append(mem_4)
print('\nThis displays the list of members having {} : '.format(course1.name), course1.member)
print('This displays the list of members having {} : '.format(course2.name), course2.member)

print('\nDisplaying the user names of members in {} : '.format(course1.name), end='')
for mem in course1.member:
    print(mem.username, end='  ')

print('\nDisplaying the user names of members in {} : '.format(course2.name), end='')
for mem in course2.member:
    print(mem.username,end='  ')
