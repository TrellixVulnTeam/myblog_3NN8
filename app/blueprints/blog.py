from flask import Blueprint,render_template,request,current_app
from app.models import Post,Category
blog_bp = Blueprint('blog',__name__)

@blog_bp.route('/')
def index():
    page = request.args.get('page',1,type=int)
    per_page = current_app.config['APP_POST_PER_PAGE']
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page,per_page=per_page)
    posts = pagination.items
    return render_template('blog/index.html',pagination=pagination,posts=posts)

@blog_bp.route('/about')
def about():
    return render_template('blog/about.html')

@blog_bp.route('/post/<int:post_id>',methods=['GET','POST'])
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('blog/post.html',post=post)


@blog_bp.route('/categories')
def categories():
    categories = Category.query.order_by(Category.id).all()
    return render_template('blog/categories.html',categories=categories)


@blog_bp.route('/category/<int:category_id>')
def show_category(category_id):
    category = Category.query.get_or_404(category_id)
    page = request.args.get('page',1,type=int)
    per_page = current_app.config['APP_POST_PER_PAGE']
    pagination = Post.query.filter_by(category_id=category_id).order_by(Post.timestamp.desc()).paginate(page,per_page=per_page)
    posts = pagination.items
    return render_template('blog/category.html',category=category,pagination=pagination,posts=posts)


@blog_bp.route('/archives')
def archives():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('blog/archives.html',posts=posts)




