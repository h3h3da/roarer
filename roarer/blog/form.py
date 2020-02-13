
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User #表单对应的模型
        fields =("username", "email") #需要渲染的控件。默认有用户名、密码、密码确认，此处增加email