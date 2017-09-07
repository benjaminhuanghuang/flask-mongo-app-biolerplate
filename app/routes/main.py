from flask import Blueprint
from flask import request, render_template, redirect

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
@main.route('/index')
def index():
    user = {'nickname': 'Lazy Gang'}  
    posts = [  
        { 
            'author': {'nickname': 'Little Horse'}, 
            'body': 'Rewriting Your Front End Every 6 Weeks' 
        },
        { 
            'author': {'nickname': 'Who'}, 
            'body': 'javascipt From Beginner to Loser' 
        },
        { 
            'author': {'nickname': 'Gig Ben'}, 
            'body': 'Writing code that Noboday Else Can Read' 
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)