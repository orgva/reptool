from  flask import render_template, request, Blueprint
from reptool.models import Post

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)

@main.route("/coin")
def coin():
    return render_template('coin.html', title='Coin')

@main.route("/company")
def company():
    return render_template('company.html', title='Company')

@main.route("/correlations")
def correlations():
    return render_template('correlations.html', title='Correlations')
