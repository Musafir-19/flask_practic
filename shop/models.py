from sqlalchemy.orm import backref, relationship
from shop import db, login_manager
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    category = db.Column(db.String(), nullable=False)
    availibility = db.Column(db.String(), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    image = db.Column(db.String(), nullable=False)
    buy = db.relationship('Buy', backref='product', lazy=True)

    def __repr__(self) -> str:
        return self.title


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False, unique=True)
    isAdmin = db.Column(db.Boolean, default=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self) -> str:
        return self.email



class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(), nullable=False)
    date_posted = db.Column(db.DateTime(), nullable=False, default=datetime.now)
    image = db.Column(db.String(), nullable=False)
    user_id  = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
    comment = db.relationship('Comment', backref='post', lazy=True)

    def __repr__(self) -> str:
            return self.title


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(), nullable=False)
    date_posted = db.Column(db.DateTime(), nullable=False, default=datetime.now)
    message = db.Column(db.String(), nullable=False)
    post_id  = db.Column(db.Integer(), db.ForeignKey('posts.id'), nullable=False)

    def __repr__(self) -> str:
            return self.subject

class Buy(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(), nullable=False)
    date_posted = db.Column(db.DateTime(), nullable=False, default=datetime.now)
    adress = db.Column(db.String(), nullable=False)
    product_id  = db.Column(db.Integer(), db.ForeignKey('products.id'))

    def __repr__(self) -> str:
            return self.email

