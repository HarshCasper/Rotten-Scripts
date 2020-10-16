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

    orders = db.relationship('Order', backref='member', lazy='dynamic')


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'))


# db.create_all()

member_obj = Member.query.filter_by(id=6).first()
print(member_obj.username)

# Adding entry in Order table
''' 
order1 = Order(price=300, member_id=member_obj.id) # by directly passing the id 
db.session.add(order1)
db.session.commit()

order2 = Order(price=500, member=member_obj)       # by using the backref and passing the object in it  
db.session.add(order2)
db.session.commit()
'''

show_data = Order.query.all()
print('Displaying data available in Order table : ',show_data)

print("\nOrder Id with corresponding Member username : ",end='')
for o in show_data:
    print(o.id, '-', o.member.username, end='     ')
