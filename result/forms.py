from flask_wtf import FlaskForm
from wtforms import ValidationError, StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, EqualTo
from result.models import User


class RegistrationForm(FlaskForm):
    username = StringField(
        'ニックネーム', 
        validators=[DataRequired()]
        )
    password = PasswordField(
        'パスワード', 
        validators=[DataRequired(),EqualTo('pass_confirm', message='パスワードが一致していません。')]
        )
    pass_confirm = PasswordField(
        'パスワード(確認)', 
        validators=[DataRequired()]
        )
    num_list = []
    for i in range(1, 41):
        num_list.append(str(i))  
    result = SelectField(
        choices=num_list
        )
    submit = SubmitField('登録')
    
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('入力されたニックネームは既に使われています。')

class LoginForm(FlaskForm):
    username = StringField(
        'ニックネーム', 
        validators=[DataRequired()]
        )
    password = PasswordField(
        'パスワード', 
        validators=[DataRequired()]
        )
    submit = SubmitField('ログイン')
    
class UpdateUserForm(FlaskForm):
    num_list = []
    for i in range(1, 41):
        num_list.append(str(i))  
    result = SelectField(
        choices=num_list
        ) 
    submit = SubmitField('更新')
    
    def __init__(self, user_id, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        self.id = user_id    
    
    
    
    