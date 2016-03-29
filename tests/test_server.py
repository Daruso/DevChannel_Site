import unittest

from server import app


class FlaskViews(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_database(self):
        resp = self.app.get('/_database')
        self.assertEqual(resp.status_code, 403)

        with self.app as clnt:
            with clnt.session_transaction() as session:
                session['username'] = 'someone_random'
            resp = self.app.get('/_database')
            self.assertEqual(resp.status_code, 403)

        with self.app as clnt:
            with clnt.session_transaction() as session:
                session['username'] = 'g4s-slack'
            resp = self.app.get('/_database')
            self.assertEqual(resp.data, b'Please specify email, username or id')

if __name__ == '__main__':
    unittest.main()
