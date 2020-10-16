from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://username:password@server/databasename"
db = SQLAlchemy(app)


class Member(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(20), nullable = False)
    join_date = db.Column(db.DateTime)


# displaying data present in table
results = Member.query.all()
for r in results:
    print("id : {}      username : {}       email : {}      password : {}       "
          "join date : {}".format(r.id, r.username, r.email, r.password, r.join_date))


# {query 1.a} filter_by() and filter query
'''
 filter() checks a conditional against a column object. 
 filter_by() finds columns which match the arguments we pass.
 # after getting object we can perform I.D.U operations (I = Insertion, D = Deletion, U = Update)
'''
obj_1 = Member.query.filter_by(id=4).first()
print("\nfilter_by : id : {}      username : {}       email : {}      password : {}       "
      "join date : {}".format(obj_1.id, obj_1.username, obj_1.email, obj_1.password, obj_1.join_date))


obj_1 = Member.query.filter(Member.id == 1).first()
print("filter :    id : {}      username : {}       email : {}      password : {}       "
      "join date : {}".format(obj_1.id, obj_1.username, obj_1.email, obj_1.password, obj_1.join_date))


# adding some values in table
'''entry = Member(username='dummy_4', email='dummy_4@gmail.com',password='surakshit_not',join_date=date.today() )
db.session.add(entry)
db.session.commit()

entry = Member(username='dummy_5', email='dummy_5@gmail.com',password='lavda_suraksit',join_date=date.today() )
db.session.add(entry)
db.session.commit()
'''

# {query 1.b} not equal to and like query
not_equal_query = Member.query.filter(Member.username != 'dummy_5')
r = not_equal_query
print('\nnot equal to query searching for data excluding username-dummy_5 : ',r.all())

like = Member.query.filter(Member.username.like('%my%'))
r = like.all()
print('like query searching for data that contain %my% in it: ',r)

# {query 1.c} in and not in query
in_query = Member.query.filter(Member.username.in_(['dummy_5', 'dummy_4'])).all()
print('\ndisplaying data having user name dummy_5 and dummy_4 : ',in_query)

not_in_query = Member.query.filter(~Member.username.in_(['dummy_5', 'dummy_4']))
q = not_equal_query.all()
print('displaying data not having user name dummy_5 and dummy_4 : ',q)

# {query 1.a} null and not null query
'''    # adding new row in data base with at least one null value in it:
entry = Member(username='dummy_6',password='lavda_suraksit',join_date=date.today() )
db.session.add(entry)
db.session.commit()'''

null_query = Member.query.filter(Member.email == None).all()
print('\ndisplaying username not having an email : ',null_query)

not_null_query = Member.query.filter(Member.email != None).all()
print('displaying username having an email : ',not_null_query)
