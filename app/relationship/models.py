from mongoengine import CASCADE

from app import db
from ..utilities.timing import utc_now_ts
from ..user.models import User


# Relationship between users
class Relationship(db.Document):
    FRIENDS = 1
    BLOCKED = -1

    RELATIONSHIP_TYPE = (
        (FRIENDS, 'Friends'),
        (BLOCKED, 'Blocked'),
    )

    PENDING = 0
    APPROVED = 1

    STATUS_TYPE = (
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
    )

    from_user = db.ReferenceField(User, db_field='fu', reversed_delete_rule=CASCADE)
    to_user = db.ReferenceField(User, db_field='tu', reversed_delete_rule=CASCADE)
    rel_type = db.IntField(db_field='rt', choices=RELATIONSHIP_TYPE)
    status = db.IntField(db_field='s', choices=STATUS_TYPE)
    req_date = db.IntField(db_field='rd', default=utc_now_ts())
    approved_date = db.IntField(db_field="ad", default=0)

    @staticmethod
    def get_relationship(from_user, to_user):
        rel = Relationship.objects.filter(from_user=from_user, to_user=to_user).first()
        if rel and rel.rel_type == Relationship.FRIENDS:
            if rel.status == Relationship.PENDING:
                return "FRIENDS_PENDING"
            if rel.status == Relationship.APPROVED:
                return "FRIENDS_APPROVED"
        elif rel and rel.rel_type == Relationship.BLOCKED:
            return "BLOCKED"
        else:
            reverse_rel = Relationship.objects.filter(from_user=to_user, to_user=from_user).first()
            if reverse_rel and reverse_rel.rel_type == Relationship.FRIENDS:
                if reverse_rel.status == Relationship.PENDING:
                    return "REVERSE_FRIENDS_PENDING"
            elif reverse_rel and reverse_rel.rel_type == Relationship.BLOCKED:
                return "REVERSE_BLOCKED"
            return None

    meta = {
        'indexes': [('from_user', 'to_user'), ('from_user', 'to_user', 'rel_type', 'status')]
    }


'''
    python manage.py shell

    from user.models import *
    from relationship.models import *
    user1 = User.objects.get(username='u1')
    user2 = User.objects.get(username='u2')
    friends = Relationship(from_user=u1, to_user=u2, rel_type=Relationship.FRIENDS, status=Relationship.PENDING).save()

    db.relationship.find()
    db.relationship.getIndexes()

'''
