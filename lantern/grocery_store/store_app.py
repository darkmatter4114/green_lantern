from flask import Flask, jsonify, request

import inject


class NoSuchUserError(Exception):
    def __init__(self, user_id):
        self.message = f'No such user_id {user_id}'


class NoSuchStoreID(Exception):
    def __init__(self, store_id):
        self.message = f'No such store_id {store_id}'


class NoSuchManagerID(Exception):
    def __init__(self, manager_id):
        self.message = f'No such manager_id {manager_id}'


app = Flask(__name__)


# @app.route('/', method = ['GET'])
# def hello():
#     return "Hello World!"

@app.errorhandler(NoSuchUserError)
def my_error_handler(e):
    return jsonify({'error': e.message}), 404


@app.errorhandler(NoSuchStoreID)
def my_error_handler(e):
    return jsonify({'error': e.message}), 404


@app.errorhandler(NoSuchManagerID)
def my_error_handler(e):
    return jsonify({'error': e.message}), 404


@app.route('/user', methods=['POST'])
def create_user():
    db = inject.instance('DB')
    user_id = db.users.add(request.json)
    return jsonify({'user_id': user_id}), 201


@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    db = inject.instance('DB')
    user = db.users.get_user_by_id(user_id)
    return jsonify(user)


@app.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    db = inject.instance('DB')
    db.users.update_user_by_id(user_id, request.json)
    return jsonify({'status': 'success'})


@app.route('/good', methods=['POST'])
def create_good():
    db = inject.instance('DB')
    good = db.goods.add(request.json)
    return jsonify({'numbers of items created': good}), 201


@app.route('/good', methods=['GET'])
def get_good():
    db = inject.instance('DB')
    good = db.goods.get_goods()
    return jsonify(good)


@app.route('/good', methods=['PUT'])
def update_good():
    db = inject.instance('DB')
    new = db.goods.update_goods(request.json)
    return jsonify({'successfully_updated': new[0],
                    'errors': {'no such id in goods': new[1]}}), 200


@app.route('/store', methods=['POST'])
def create_store():
    db = inject.instance('DB')
    id = db.stores.add(request.json)
    return jsonify({'store_id': id}), 201


@app.route('/store/<int:id>', methods=['GET'])
def get_store(id):
    db = inject.instance('DB')
    store = db.stores.get_stores_by_id(id)
    return jsonify(store)


@app.route('/store/<int:id>', methods=['PUT'])
def update_store(id):
    db = inject.instance('DB')
    db.stores.update_stores(request.json, id)
    return jsonify({'status': 'success'}), 200
