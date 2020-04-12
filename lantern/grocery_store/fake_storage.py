from itertools import count
from store_app import NoSuchUserError
from store_app import NoSuchStoreID
from store_app import NoSuchManagerID


class FakeStorage:
    def __init__(self):
        self._users = FakeUsers()
        self._goods = FakeGoods()
        self._stores = FakeStores()

    @property
    def users(self):
        return self._users

    @property
    def goods(self):
        return self._goods

    @property
    def stores(self):
        return self._stores


class FakeUsers:
    def __init__(self):
        self._users = {}
        self._id_counter = count(1)

    def add(self, user):
        user_id = next(self._id_counter)
        self._users[user_id] = user
        return user_id

    def get_user_by_id(self, user_id):
        try:
            return self._users[user_id]
        except KeyError:
            raise NoSuchUserError(user_id)

    def update_user_by_id(self, user_id, user):
        if user_id in self._users:
            self._users[user_id] = user
        else:
            raise NoSuchUserError(user_id)


class FakeGoods:
    def __init__(self):
        self._goods = {}
        self._id_counter = count(1)

    def add(self, good):
        goods_id = next(self._id_counter)
        self._goods[goods_id] = good
        return len(self._goods)

    def get_goods(self):

        good = self._goods
        try:
            return good
        except KeyError:
            raise NoSuchUserError()

    def update_goods(self, goods):
        no_id = []
        upd = 0
        g_key = self._goods.items()
        for x, y in g_key:
            if goods['id'] == y.get('id'):
                y = goods
                upd += 1
            elif goods['id'] != y.get('id'):
                no_id.append(goods['id'])
        return upd, no_id


class FakeStores:
    def __init__(self):
        self._stores = {}
        self._id_counter = count(1)

    def add(self, stores):
        try:
            id = next(self._id_counter)
            self._stores[id] = stores
            return id
        except KeyError:
            raise NoSuchStoreID(id)

    def get_stores_by_id(self, id):
        try:
            return self._stores[id]
        except KeyError:
            raise NoSuchStoreID(id)

    def update_stores(self, stores, id):
        if id in self._stores:
            self._stores[id] = stores
        else:
            return NoSuchStoreID(stores['id'])

