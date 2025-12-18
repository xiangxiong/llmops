from flask_wtf import FlaskForm;
from wtforms import StringField;
from wtforms.validators import  DataRequired,Length;

class CompletionReq(FlaskForm):

    # 必填，长度 20
    query = StringField("query",
                        validators=[
                            DataRequired(message="用户提问式必填的"),
                            Length(max=20,message="用户提问式长度不能超过20个字符")
                        ])