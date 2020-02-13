# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required

from django import forms
from captcha.fields import CaptchaField  # 导入模块
from django.http import HttpResponse
from .form import RegisterForm

class captcha_class(forms.Form):
    ''' 验证码功能类'''
    captcha = CaptchaField(label='验证码')



def login(request):
    ''' 用户登录页面 '''
    captcha_ = captcha_class()
    return render(request, "login.html", {"captcha": captcha_})

# def login_check(request):
#     """ 登录校验 """
#     captcha_ = captcha_class(request.POST)
#     if captcha_.is_valid():
#         ''' 图片验证码校验成功 '''
#         pass
#
#     return login_.login(request)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', context={'form': form})

@login_required()
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
