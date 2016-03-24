import unittest
import json

from tinydb import TinyDB, Query

from apps import database, invite


class Database(unittest.TestCase):
    DB_NAME = 'test_database.json'

    @classmethod
    def setUpClass(cls):
        cls.db = TinyDB(cls.DB_NAME)
        cls.db.insert_multiple([
            {"skills": 'python', "github": 'https://github.com/kennethreitz', "time": '0',  "points": '',
             "email": 'kennethreitz@test.ru', "username": 'kennethreitz', 'slack_id': 'U123456789'},
            {"skills": 'Duchess', "github": 'https://bitbucket.org/madhatter', "time": '5',  "points": '1871',
             "email": 'alice@looking-glass.thru', "username": 'cheshirecat', 'slack_id': 'U18651871'}
        ])
        cls.User = Query()
        database.db = cls.db
        database.User = cls.User

    @classmethod
    def tearDownClass(cls):
        cls.db.close()
        import os
        os.remove(cls.DB_NAME)

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


class Invite(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
