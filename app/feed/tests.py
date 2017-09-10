from app import create_app
from mongoengine.connection import _get_db
import unittest
from flask import session

from ..user.models import User
from ..relationship.models import Relationship

class FeedTest(unittest.TestCase):
    def setUp(self):
        self.flask_app = create_app('test')
        self.test_client = self.flask_app.test_client()

    def tearDown(self):
        db = _get_db()
        db.client.drop_database(db)

    def user1_dict(self):
        return dict(
            first_name="Jorge",
            last_name="Escobar",
            username="jorge",
            email="jorge@example.com",
            password="test123",
            confirm="test123"
            )

    def user2_dict(self):
        return dict(
            first_name="Javier",
            last_name="Escobar",
            username="javier",
            email="javier@example.com",
            password="test123",
            confirm="test123"
            )

    def user3_dict(self):
        return dict(
            first_name="Luis",
            last_name="Escobar",
            username="luiti",
            email="luiti@example.com",
            password="test123",
            confirm="test123"
            )

    def test_feed_posts(self):
        # register user
        rv = self.test_client.post('/register', data=self.user1_dict(),
            follow_redirects=True)

        # login the first user
        rv = self.test_client.post('/login', data=dict(
            username=self.user1_dict()['username'],
            password=self.user1_dict()['password'],
            ))

        # post a message
        rv = self.test_client.post('/message/add', data=dict(
            post="Test Post #1 User 1",
            to_user=self.user1_dict()['username']
            ), follow_redirects=True)
        assert "Test Post #1 User 1" in str(rv.data)

        # register user #2
        rv = self.test_client.post('/register', data=self.user2_dict(),
            follow_redirects=True)

        # make friends with user #2
        rv = self.test_client.get('/add_friend/' + self.user2_dict()['username'],
            follow_redirects=True)

        # login user #2 and confirm friend user #1
        rv = self.test_client.post('/login', data=dict(
            username=self.user2_dict()['username'],
            password=self.user2_dict()['password'],
            ))
        rv = self.test_client.get('/add_friend/' + self.user1_dict()['username'],
            follow_redirects=True)

        # login the first user again
        rv = self.test_client.post('/login', data=dict(
            username=self.user1_dict()['username'],
            password=self.user1_dict()['password'],
            ))

        # post a message
        rv = self.test_client.post('/message/add', data=dict(
            post="Test Post #2 User 1",
            to_user=self.user1_dict()['username']
            ), follow_redirects=True)
        assert "Test Post #2 User 1" in str(rv.data)

        # post a message to user 2
        rv = self.test_client.post('/message/add', data=dict(
            post="Test Post User 1 to User 2",
            to_user=self.user1_dict()['username']
            ), follow_redirects=True)

        # login the second user
        rv = self.test_client.post('/login', data=dict(
            username=self.user2_dict()['username'],
            password=self.user2_dict()['password'],
            ))
        rv = self.test_client.get('/')
        assert "Test Post #2 User 1" in str(rv.data)
        assert "Test Post User 1 to User 2" in str(rv.data)

        # register user #3
        rv = self.test_client.post('/register', data=self.user3_dict(),
            follow_redirects=True)

        # make friends with user #2
        rv = self.test_client.get('/add_friend/' + self.user2_dict()['username'],
            follow_redirects=True)

        # login the first user
        rv = self.test_client.post('/login', data=dict(
            username=self.user1_dict()['username'],
            password=self.user1_dict()['password'],
            ))

        # block user 3
        rv = self.test_client.get('/block/' + self.user3_dict()['username'],
            follow_redirects=True)

        # login the second user
        rv = self.test_client.post('/login', data=dict(
            username=self.user2_dict()['username'],
            password=self.user2_dict()['password'],
            ))

        # user 2 confirm friend user 3
        rv = self.test_client.get('/add_friend/' + self.user3_dict()['username'],
            follow_redirects=True)

        # post a message to user 3
        rv = self.test_client.post('/message/add', data=dict(
            post="Test Post User 2 to User 3",
            to_user=self.user3_dict()['username']
            ), follow_redirects=True)

        # login the first user
        rv = self.test_client.post('/login', data=dict(
            username=self.user1_dict()['username'],
            password=self.user1_dict()['password'],
            ))

        # check he doesn't see user 2's post to user 3 (blocked)
        rv = self.test_client.get('/')
        assert "Test Post User 2 to User 3" not in str(rv.data)