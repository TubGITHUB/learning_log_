from django.shortcuts import render, reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect


# Create your views here.


def logout_view(request):
    """用户登出"""
    logout(request)
    return HttpResponseRedirect(reverse("learning_logs:index"))

def register(request):
    """用户注册"""
    if request.method != "POST":
        form = UserCreationForm()
    else:
        # 处理填写好的表单
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            # 让用户自动登录，再重定向到首页
            authenticate_user = authenticate(username=new_user.username,
                                             password=request.POST["password1"])
            login(request, authenticate_user)
            return HttpResponseRedirect(reverse("learning_logs:index"))
    context = {"form": form}
    return render(request, "users/register.html", context)