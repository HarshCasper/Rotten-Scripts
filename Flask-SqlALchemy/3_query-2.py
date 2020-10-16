from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://username:password@server/databasename"
db = SQLAlchemy(app)


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(20), nullable = False)
    join_date = db.Column(db.DateTime)


q = Member.query

# {query 2.a } and query : for finding results
and_query = q.filter(db.and_(Member.email == 'dummy@dummy.com', Member.username == 'dummy_king')).all()
print('displaying result dor having email dummy@dummy.com and username dummy_king : ',and_query)

# {query 2.b } or query : for finding results
or_query = q.filter(db.or_(Member.email == 'dummy@dummy.com', Member.email == None)).all()
print('displaying result dor having email dummy@dummy.com or no email at all : ',or_query)

# {query 2.c } order_by query : for arranging the results
arrange = q.order_by(Member.email).all()
print('\narranged by email : ', arrange)
arrange = q.order_by(Member.username).all()
print('arranged by username : ', arrange)
arrange = q.order_by(Member.id).all()
print('arranged by id : ', arrange)
arrange = q.order_by(Member.username).first()
print('alphabetical first username : ', arrange.username)

# {query 2.d } limit query : for displaying limited results only
lim = q.limit(2).all()
print('\ndisplaying starting two results ',lim)
lim = q.order_by(Member.username).limit(2).all()
print('arranging according to username and the displaying first 2 result : ', lim)

# {query 2.e } offset query : for skipping the specified result
offset = q.offset(2).all()
print('\nskipping starting two results thn displaying rest of it : ',offset)
offset = q.order_by(Member.username).offset(2).limit(1).all()
print('arranging according to username then skipping first 2 results and the displaying rest of result : ',offset)

# {query 2.f } count query : show the number of results in tha query
count_query = q.count()
print('\ncounting number of data : ',count_query)
