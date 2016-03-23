import unittest

from tinydb import TinyDB

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

    @classmethod
    def tearDownClass(cls):
        del cls.db
        import os, time
        time.sleep(2)
        os.remove(cls.DB_NAME)


class Invite(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
