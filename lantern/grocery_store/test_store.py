import inject

from store_app import app
from fake_storage import FakeStorage


def configure_test(binder):
    db = FakeStorage()
    binder.bind('DB', db)


class Initializer:
    def setup(self):
        inject.clear_and_configure(configure_test)
        app.config['TESTING'] = True
        with app.test_client() as client:
            self.client = client


class TestUsers(Initializer):
    def test_create_new(self):
        resp = self.client.post(
            '/user',
            json={'name': 'John Doe'}
        )
        assert resp.status_code == 201
        assert resp.json == {'user_id': 1}

        resp = self.client.post(
            '/user',
            json={'name': 'Andrew Derkach'}
        )
        assert resp.json == {'user_id': 2}

    def test_successful_get_user(self):
        resp = self.client.post(
            '/user',
            json={'name': 'John Doe'}
        )
        user_id = resp.json['user_id']
        resp = self.client.get(f'/user/{user_id}')
        assert resp.status_code == 200
        assert resp.json == {'name': 'John Doe'}

    def test_get_unexistent_user(self):
        resp = self.client.get(f'/user/1')
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such user_id 1'}

    def test_succesfull_update_user(self):
        resp = self.client.post(
            '/user',
            json={'name': 'John Doe'}
        )
        user_id = resp.json['user_id']
        resp = self.client.put(
            '/user/1',
            json={'name': 'Johanna Doe'}
        )
        assert resp.status_code == 200
        assert resp.json == {'status': 'success'}

    def test_unexistent_update_user(self):
        resp = self.client.put(
            f'/user/1',
            json={'name': 'Johanna Doe'}
        )
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such user_id 1'}


class TestGoods(Initializer):
    def test_create_new(self):
        resp = self.client.post(
            '/good',
            json={'name': 'Chocolate_bar', 'price': 10}
        )
        assert resp.status_code == 201
        assert resp.json == {'numbers of items created': 1}

    def test_successful_get_good(self):
        resp = self.client.post(
            '/good'
        )
        good_id = resp.json
        resp = self.client.get(f'/good')
        assert resp.status_code == 200
        # assert resp.json == {'name': 'Chocolate_bar', 'price': 10, 'id': 1}

    # def test_get_unexistent_user(self):
    #     resp = self.client.get(f'/good')
    #     assert resp.status_code == 404

    def test_succesfull_update_good(self):
        resp = self.client.post(
            '/good',
            json={'name': 'Chocolate_bar', 'price': 10, 'id': 1

                  }
        )
        # resp = self.client.post(
        #     '/good',
        #     json={'name': 'Chocolate_bar', 'price': 13, 'id': 2
        #
        #           }
        # )
        resp = self.client.put(
            '/good',
            json={'name': 'Chocolate_bar', 'price': 11, 'id': 1}
        )
        assert resp.status_code == 200
        assert resp.json == ({'successfully_updated': 1,
                              'errors': {'no such id in goods': []}})


class TestStores(Initializer):
    def test_create_new(self):
        resp = self.client.post(
            '/store',
            json={'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 2}
        )
        assert resp.status_code == 201
        assert resp.json == {'store_id': 1}

    def test_successful_get_store(self):
        resp = self.client.post(
            '/store',
            json={'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 2}
        )
        id = resp.json['store_id']
        resp = self.client.get(f'/store/{id}')
        assert resp.status_code == 200
        assert resp.json == {'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 2}

    def test_get_unexistent_store(self):
        resp = self.client.get(f'/store/3')
        assert resp.status_code == 404

    def test_succesfull_update_stores(self):
        resp = self.client.post(
            '/store',
            json={'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 2}
        )
        resp = self.client.put(
            '/store/1',
            json={'name': 'Local Taste', 'location': 'Lviv', 'manager_id': 2}
        )
        # assert resp.json == {'name': 'Local Taste', 'location': 'Lviv', 'manager_id': 2}

        assert resp.status_code == 200
        assert resp.json == {'status': 'success'}

    def test_unsuccesfull_update_stores(self):
        resp = self.client.get(f'/store/3')
        assert resp.status_code == 404
