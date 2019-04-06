from wtforms import Form, PasswordField, StringField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(Form):
    username = StringField('用户名', validators=[DataRequired(), Length(1, 20),
                                              Email(message='用户名不符合规范')])
    password = PasswordField('密码', validators=[
        DataRequired(message='密码不可以为空，请输入你的密码')])


class SignUpForm(LoginForm):
    nickname = StringField('昵称', validators=[DataRequired(), Length(1, 20)])
    sex = StringField('性别', validators=[DataRequired(), Length(1, 2)])
    grade = StringField('年级', validators=[DataRequired(), Length(1, 2)])
