#-*- coding:utf8 -*-

from django.conf.urls import url

import api

#-------------------------用户模块------------------------
urlpatterns = [
    url(r'^myuser/signUp$', api.SignUpApi.as_view()),  #注册用户
    url(r'^myuser/signIn$', api.SignInApi.as_view()),  #用户登录
    url(r'^myuser/postEmailUrl$', api.PostEmailUrlApi.as_view()), #发送重置链接到邮箱
]



