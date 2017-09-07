from flask import Blueprint
from flask import request, render_template, redirect

user = Blueprint('user', __name__)

@user.route('/user/index')
def index():
    users = [  
        {'name': 'Little Horse'}, 
        {'name': 'Who'}, 
        {'name': 'Gig Ben'}
    ]
    return render_template("userlist.html",
                           title='User List',
                           users=users)