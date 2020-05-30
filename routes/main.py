import json
from datetime import datetime
from pprint import pprint

from flask import Blueprint, render_template, jsonify
from grocery_store.database import db
from flask_login import current_user, login_required

from grocery_store.models import Good, Store, User, Order, OrderLine

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    # stores = Store.query.filter(Store.manager_id == 63)
    stores = Store.query.filter(Store.manager_id == current_user.user_id).all()
    return render_template('profile.html',
                           user=current_user.name,
                           email=current_user.email,
                           stores=stores)


@main.route('/good', methods=['GET'])
def gd():
    return render_template('goods.html', items=Good.query.all())


@main.route('/store', methods=['GET'])
def st():
    return render_template('store.html', items=Store.query.all())


@main.route('/st_detail/<name>')
def detail(name=None):
    if name:
        return render_template('detail.html', items=Store.query.filter_by(name=name))
    return render_template('detail.html')


@main.route('/orders')
@login_required
def orders():
    orders = Order.query.filter(Order.user_id == current_user.user_id).all()
    order_ = {}

    for order in orders:
        a = []
        b = []
        order_[order.order_id] = {}
        order_[order.order_id]['date'] = order.created_time
        store = Store.query.filter(Store.store_id == order.store_id).first()
        order_[order.order_id]['store_n'] = store.name
        order_[order.order_id]['name_g'] = {}
        order_lines = OrderLine.query.filter(order.order_id == OrderLine.order_id).all()
        for order_line in order_lines:
            goods = Good.query.filter(Good.good_id == order_line.good_id).all()
            for good in goods:
                a.append(good.name)
                b.append(good.price)
                suma = sum(b)
                order_[order.order_id]['name_g'] = dict(zip(a[::], b[::]))
        order_[order.order_id]['sum'] = suma
                # order_[order.order_id]['price_g'] = b good.price
        #         order_[order.order_id].update(dict=gn)
    return render_template('orders.html',
                           orders=order_)
