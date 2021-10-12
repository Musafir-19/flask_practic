from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
import email_validator
from shop.models import User
from flask_wtf.file import FileField, FileAllowed  


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired("Это поле обязательно"), Email("Не правильный email - адрес")]) 
    password = PasswordField('Пароль', validators=[DataRequired("Это поле обязательно"), Length(min=8, max=20, message='Пароль должен быть > 8 < 20')])
    confirm_password = PasswordField('Подтверждение пароля', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Регистрация')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Такой email уже существует!')

class PostForm(FlaskForm):
    title  = StringField('Заголовок', validators=[DataRequired()])
    content = TextAreaField('Контент', validators=[DataRequired()]) 
    image = FileField('Картинка поста', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Создать пост')