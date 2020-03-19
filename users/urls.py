from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = "users"

urlpatterns = [
    path(r"login/", LoginView.as_view(template_name="users/login.html"), name="login"),     # 登录
    path(r"logout/", views.logout_view, name="logout"),                                       # 登出
    path(r"register/", views.register, name="register"),                                      # 注册

]

