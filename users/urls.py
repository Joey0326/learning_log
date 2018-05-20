from django.urls import path,re_path
from django.contrib.auth.views import login
from . import views
urlpatterns = [
    #登录界面
    re_path(r'^login/$',login,{'template_name':'users/login.html'},name = 'login'),
    #注销页面
    re_path(r'^logout/$',views.logout_view,name = 'logout'),
    #注册页面
    re_path(r'^register/$',views.register,name = 'register'),
]
app_name = 'users'
