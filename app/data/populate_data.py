import csv
import os


def get_users():
    with open(os.getcwd()+'/app/data/users.csv', 'r') as f:
        reader = csv.DictReader(f)
        users = [i for i in reader]
        return users


def get_goods():
    with open(os.getcwd()+'/app/data/goods.csv', 'r') as f:
        reader = csv.DictReader(f)
        goods = [i for i in reader]
        return goods


def get_stores():
    with open(os.getcwd()+'/app/data/stores.csv', 'r') as f:
        reader = csv.DictReader(f)
        stores = [i for i in reader]
        return stores
