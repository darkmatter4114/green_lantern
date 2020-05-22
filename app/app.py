from flask import Flask, jsonify
from sqlalchemy_utils import create_database, database_exists

from app.models.db_models import db, Users, Goods, Stores

from app.config import Config
from app.data.populate_data import get_users, get_goods, get_stores

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


@app.route('/users', methods=['GET'])
def get():
   return 'database create'


with app.app_context():
    if database_exists(db.engine.url):
        db.create_all()
        print('Database exists')
    else:
        print(f"Database does not exists {db.engine.url}")
        create_database(db.engine.url)
        print('Data base created')

with app.app_context():
    users = get_users()
    for user in users:
        db.session.add(Users(**user))
    db.session.commit()
    print('Data written in data_base succesfuly')

with app.app_context():
    goods = get_goods()
    for goods in goods:
        db.session.add(Goods(**goods))
    db.session.commit()
    print('Data written in data_base succesfuly')

with app.app_context():
    stores = get_stores()
    for stores in stores:
        db.session.add(Stores(**stores))
    db.session.commit()
    print('Data written in data_base succesfuly')
