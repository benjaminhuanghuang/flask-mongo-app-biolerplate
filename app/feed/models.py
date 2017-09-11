from mongoengine import CASCADE
from flask import url_for, current_app
import os

from app import db
from ..utilities.timing import utc_now_ts_ms, ms_stamp_humanize
from ..user.models import User
from ..utilities.common import linkify

POST = 1
COMMENT = 2
LIKE = 3

MESSAGE_TYPE = (
    (POST, 'Post'),
    (COMMENT, 'Comment'),
    (LIKE, 'Like'),
)


class Message(db.Document):
    from_user = db.ReferenceField(User, db_field="from_user", reverse_delete_rule=CASCADE)
    to_user = db.ReferenceField(User, db_field="to_user", default=None, reverse_delete_rule=CASCADE)
    text = db.StringField(db_field="text", max_length=1024)
    live = db.BooleanField(db_field="live", default=None)
    create_date = db.LongField(db_field="create_date", default=utc_now_ts_ms())
    parent = db.ObjectIdField(db_field="parent", default=None)
    images = db.ListField(db_field="images")
    message_type = db.IntField(db_field='message_type', default=POST, choices=MESSAGE_TYPE)

    @property
    def text_linkified(self):
        return linkify(self.text)

    @property
    def human_timestamp(self):
        return ms_stamp_humanize(self.create_date)

    @property
    def comments(self):
        return Message.objects.filter(parent=self.id, message_type=COMMENT).order_by('create_date')

    @property
    def likes(self):
        return Message.objects.filter(parent=self.id, message_type=LIKE).order_by('-create_date')

    def post_imgsrc(self, image_ts, size):
        return url_for('static', filename=os.path.join('images', 'posts', '%s.%s.%s.png' % (self.id, image_ts, size)))

    meta = {
        'indexes': [('from_user', 'to_user', '-create_date', 'parent', 'message_type', 'live')]
    }


class Feed(db.Document):
    # the owner of the message
    user = db.ReferenceField(User, db_field="user", reverse_delete_rule=CASCADE)
    message = db.ReferenceField(Message, db_field="message", reverse_delete_rule=CASCADE)
    create_date = db.LongField(db_field="create_date", default=utc_now_ts_ms())

    meta = {
        'indexes': [('user', '-create_date')]
    }
