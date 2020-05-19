from flask import Blueprint, render_template
from grocery_store.database import db
from flask_login import current_user

from grocery_store.models import Good, Store

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
def profile():
    return render_template('profile.html', user=current_user.name, email=current_user.email)


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
