'''
Test suit for user module
'''
from app import create_app
from mongoengine.connection import _get_db
import unittest
from flask import session

from .models import User

class UserTest(unittest.TestCase):

    def setUp(self):
        self.flask_app = create_app('test')
        self.test_client = self.flask_app.test_client()

    def tearDown(self):
        db = _get_db()
        db.client.drop_database(db)

    def user_dict(self):
        return dict(
            first_name="Jorge",
            last_name="Escobar",
            username="jorge",
            email="jorge@example.com",
            password="test123",
            confirm="test123"
            )
    # @unittest.skip("skipping")
    def test_register_user(self):
        # basic registration
        rv = self.test_client.post('/register', data=self.user_dict(), follow_redirects=True)
        assert User.objects.filter(username=self.user_dict()['username']).count() == 1

    # @unittest.skip("skipping")
    def test_register_user_invalid_char(self):
        # Invalid username characters
        user2 = self.user_dict()
        user2['username'] = "test test"
        user2['email'] = "test@example.com"
        rv = self.test_client.post('/register', data=user2, follow_redirects=True)
        assert "Invalid username" in str(rv.data)

    # @unittest.skip("skipping")
    def test_register_user_lowercase(self):
        # Is username being saved in lowercase?
        user3 = self.user_dict()
        user3['username'] = "TestUser"
        user3['email'] = "test2@example.com"
        rv = self.test_client.post('/register', data=user3, follow_redirects=True)
        assert User.objects.filter(username=user3['username'].lower()).count() == 1

    def test_register_user_confirm(self):
        user = self.user_dict()
        user['username'] = "testuser"
        user['email'] = "test2@example.com"
        rv = self.test_client.post('/register', data=user, follow_redirects=True)
        # confirm the user
        user = User.objects.get(username=user['username'])
        code = user.change_configuration.get('confirmation_code')
        rv = self.test_client.get('/confirm/' + user.username + '/' + code)
        assert "Your email has been confirmed" in str(rv.data)

        # try again to confirm
        rv = self.test_client.get('/confirm/' + user.username + '/' + code)
        assert rv.status_code == 404

        # check change configuration is empty
        user = User.objects.get(username=user['username'])
        assert user.change_configuration == {}

    # @unittest.skip("skipping")
    def test_login_user(self):
        # create user
        self.test_client.post('/register', data=self.user_dict())
        # login user
        rv = self.test_client.post('/login', data=dict(
            username=self.user_dict()['username'],
            password=self.user_dict()['password']
            ))
        # check the session is set
        with self.test_client as c:
            rv = c.get('/')
            assert session.get('username') == self.user_dict()['username']

    # @unittest.skip("skipping")
    def test_edit_profile(self):
        # create a user
        self.test_client.post('/register', data=self.user_dict())

        # confirm the user
        user = User.objects.get(username=self.user_dict()['username'])
        code = user.change_configuration.get('confirmation_code')
        rv = self.test_client.get('/confirm/' + user.username + '/' + code)

        # login the user
        rv = self.test_client.post('/login', data=dict(
            username=self.user_dict()['username'],
            password=self.user_dict()['password']
            ))

        # check that user has edit button on his own profile
        rv = self.test_client.get('/' + self.user_dict()['username'])
        assert "Edit profile" in str(rv.data)

        # edit fields
        user = self.user_dict()
        user['first_name'] = "Test First"
        user['last_name'] = "Test Last"
        user['username'] = "TestUsername"

        # edit the user
        rv = self.test_client.post('/edit', data=user)
        assert "Profile updated" in str(rv.data)
        edited_user = User.objects.first()

        assert edited_user.first_name == "Test First"
        assert edited_user.last_name == "Test Last"
        assert edited_user.username == "testusername"

        # check new email is in change configuration
        user['email'] = "test@example.com"
        rv = self.test_client.post('/edit', data=user)
        assert "You will need to confirm the new email to complete this change" in str(rv.data)
        db_user = User.objects.first()
        code = db_user.change_configuration.get('confirmation_code')
        new_email = db_user.change_configuration.get('new_email')
        assert new_email == user['email']

        # now confirm
        rv = self.test_client.get('/confirm/' + db_user.username + '/' + code)
        db_user = User.objects.first()
        assert db_user.email == user['email']
        assert db_user.change_configuration == {}

        # create a second user
        self.test_client.post('/register', data=self.user_dict())
        # login the user
        rv = self.test_client.post('/login', data=dict(
            username=self.user_dict()['username'],
            password=self.user_dict()['password']
            ))

        # try to save same email
        user = self.user_dict()
        user['email'] = "test@example.com"
        rv = self.test_client.post('/edit', data=user)
        assert "Email already exists" in str(rv.data)

        # try to save same username
        user = self.user_dict()
        user['username'] = "TestUsername"
        rv = self.test_client.post('/edit', data=user)
        assert "Username already exists" in str(rv.data)

    # @unittest.skip("skipping")
    def test_get_profile(self):
        # create a user
        self.test_client.post('/register', data=self.user_dict())

        # get the user's profile
        rv = self.test_client.get('/' + self.user_dict()['username'])
        assert self.user_dict()['username'] in str(rv.data)

        # get a 404
        rv = self.test_client.get('/noexist')
        assert rv.status_code == 404

    # @unittest.skip("skipping")
    def test_forgot_password(self):
        # create a user
        self.test_client.post('/register', data=self.user_dict())

        # confirm the user
        user = User.objects.get(username=self.user_dict()['username'])
        code = user.change_configuration.get('confirmation_code')
        rv = self.test_client.get('/confirm/' + user.username + '/' + code)

        # enter user forgot email
        rv = self.test_client.post('/forgot', data=dict(email=self.user_dict().get('email')))
        user = User.objects.first()
        password_reset_code = user.change_configuration.get('password_reset_code')
        assert password_reset_code is not None

        # try wrong username
        rv = self.test_client.get('/password_reset/not_there/' + password_reset_code)
        assert rv.status_code == 404

        # try wrong password reset code
        rv = self.test_client.get('/password_reset/' + self.user_dict().get('username') + '/bad-code')
        assert rv.status_code == 404

        # do right password reset code
        rv = self.test_client.post('/password_reset/' +self.user_dict().get('username') + '/' + password_reset_code,
        data=dict(password='newpassword', confirm='newpassword'), follow_redirects=True)
        assert "Your password has been updated" in str(rv.data)
        user = User.objects.first()
        assert user.change_configuration == {}

        # try logging in with new password
        rv = self.test_client.post('/login', data=dict(
            username=self.user_dict()['username'],
            password='newpassword'
            ))
        # check the session is set
        with self.test_client as c:
            rv = c.get('/')
            assert session.get('username') == self.user_dict()['username']

    @unittest.skip("skipping")
    def test_change_password(self):
        # create a user
        self.test_client.post('/register', data=self.user_dict())

        # confirm the user
        user = User.objects.get(username=self.user_dict()['username'])
        code = user.change_configuration.get('confirmation_code')
        rv = self.test_client.get('/confirm/' + user.username + '/' + code)

        # login the user
        rv = self.test_client.post('/login', data=dict(
            username=self.user_dict()['username'],
            password=self.user_dict()['password']
            ))

        # change the password
        rv = self.test_client.post('/change_password', data=dict(
            current_password=self.user_dict()['password'],
            password="newpassword",
            confirm="newpassword"
            ), follow_redirects=True)
        assert "Your password has been updated" in str(rv.data)

        # try logging in with new password
        # try logging in with new password
        rv = self.test_client.post('/login', data=dict(
            username=self.user_dict()['username'],
            password='newpassword'
            ))
        # check the session is set
        with self.app as c:
            rv = c.get('/')
            assert session.get('username') == self.user_dict()['username']
