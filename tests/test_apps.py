import unittest
import json

from tinydb import TinyDB, Query

from website.apps import database, invite


class Database(unittest.TestCase):
    DB_NAME = 'test_database.json'

    def setUp(self):
        self.db = TinyDB(self.DB_NAME)
        self.db.insert_multiple([
            {"skills": 'python', "github": 'https://github.com/kennethreitz', "time": '0',  "points": '',
             "email": 'kennethreitz@test.ru', "username": 'kennethreitz', 'slack_id': 'U123456789'},
            {"skills": 'Duchess', "github": 'https://bitbucket.org/madhatter', "time": '5',  "points": '1871',
             "email": 'alice@looking-glass.thru', "username": 'cheshirecat', 'slack_id': 'U18651871'}
        ])
        self.User = Query()
        database.db = self.db
        database.User = self.User

    def tearDown(self):
        self.db.close()
        import os
        os.remove(self.DB_NAME)

    def test_insert_user(self):
        self.assertDictEqual(
            json.loads(database.insert_user(email='wonder@land.al', skills='magic, rabbits'))['response'],
            dict(skills='magic, rabbits', github='', time='', email='wonder@land.al', username='', slack_id='', points='0')
        )

    def test_update_user(self):
        self.assertDictEqual(
            json.loads(database.update_user(params={'skills': 'requests'}, slack_id='U123456789'))['response']['value'],
            {"skills": 'requests', "github": 'https://github.com/kennethreitz', "time": '0',  "points": '',
             "email": 'kennethreitz@test.ru', "username": 'kennethreitz', 'slack_id': 'U123456789'}
        )
        self.assertDictEqual(
            json.loads(database.update_user(params={'username': 'kz'}, slack_id='U123456789'))['response']['value'],
            {"skills": 'requests', "github": 'https://github.com/kennethreitz', "time": '0',  "points": '',
             "email": 'kennethreitz@test.ru', "username": 'kz', 'slack_id': 'U123456789'}
        )
        self.assertEqual(
            json.loads(database.update_user(params={'skills': 'django'}, slack_id='nonExisting'))['response']['value'],
            None
        )

    def test_get_user(self):
        self.assertDictEqual(
            json.loads(database.get_user(slack_id='U18651871'))['response'],
            {"skills": 'Duchess', "github": 'https://bitbucket.org/madhatter', "time": '5',  "points": '1871',
             "email": 'alice@looking-glass.thru', "username": 'cheshirecat', 'slack_id': 'U18651871'}
        )
        self.assertDictEqual(
            json.loads(database.get_user(slack_id='U123456789', email='alice@looking-glass.thru'))['response'],
            {"skills": 'python', "github": 'https://github.com/kennethreitz', "time": '0',  "points": '',
             "email": 'kennethreitz@test.ru', "username": 'kennethreitz', 'slack_id': 'U123456789'}
        )
        self.assertDictEqual(
            json.loads(database.get_user(email='wonder@land.al'))['response'],
            {'Error': 'User not found'}
        )

    def test_get_all_users(self):
        self.assertListEqual(
            json.loads(database.get_all_users())['response'],
            [
                {"skills": 'python', "github": 'https://github.com/kennethreitz', "time": '0',  "points": '',
                 "email": 'kennethreitz@test.ru', "username": 'kennethreitz', 'slack_id': 'U123456789'},
                {"skills": 'Duchess', "github": 'https://bitbucket.org/madhatter', "time": '5',  "points": '1871',
                 "email": 'alice@looking-glass.thru', "username": 'cheshirecat', 'slack_id': 'U18651871'}
            ]
        )

    def test_delete_user(self):
        self.assertEqual(
            json.loads(database.delete_user(slack_id='U123456789', email='alice@looking-glass.thru', username='cheshirecat'))['response']['id'],
            'U123456789'
        )
        self.assertEqual(
            json.loads(database.delete_user(email='alice@looking-glass.thru', username='cheshirecat'))['response']['id'],
            'cheshirecat'
        )


class Invite(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
