from shop import app
from flask import render_template
from shop.models import Product


@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)


@app.route('/blog')
def blog():
    return render_template('blog.html')
