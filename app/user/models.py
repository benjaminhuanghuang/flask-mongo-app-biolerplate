from app import db
from ..utilities.timing import utc_now_ts

class User(db.Document):
    username = db.StringField(db_field="user_name", required=True, unique=True)
    password = db.StringField(db_field="password", required=True)
    email = db.EmailField(db_field="email", required=True, unique=True)
    first_name = db.StringField(db_field="first_name", max_length=50)
    last_name = db.StringField(db_field="last_name", max_length=50)
    created_at = db.IntField(db_field="created_at", default=utc_now_ts())
    bio = db.StringField(db_field="bio", max_length=160)
    email_confirmed = db.BooleanField(db_field="email_confirmed", default=False)
    change_configuration = db.DictField(db_field="change_config")
    avatar = db.StringField(db_field="avatar", default=None)

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.username = document.username.lower()
        document.email = document.email.lower()

