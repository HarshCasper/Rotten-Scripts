# make sure to un-comment a code before using it !!!


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


# db.create_all()   # creating table command

# adding values :
'''
# entry_1 = Member(username='dummy_king', email='dummy@dummy.com',password='surakshit',join_date=date.today() )
# db.session.add(entry_1)
# db.session.commit()

# entry_2 = Member(username='dummy_queen', email='pussy@dummy.com',password='surakshit',join_date=date.today() )
# db.session.add(entry_2)
# db.session.commit()

# entry_3 = Member(username='dummy_3', email='p3u3s3s3y3@dummy.com',password='surakshit',join_date=date.today() )
# db.session.add(entry_3)
# db.session.commit()
'''

# updating values :
'''
object_of_class_using_for_updating = Member.query.filter_by(id=1).first()
object_of_class_using_for_updating.password = 'surakshit'
db.session.commit()

object_of_class_using_for_updating = Member.query.filter_by(id=2).first()
object_of_class_using_for_updating.password = 'diwani'
db.session.commit()
'''

# deleting values :
'''
object_of_class_using_for_delete = Member.query.filter_by(id=2).first()
db.session.delete(object_of_class_using_for_delete)
db.session.commit()
'''
