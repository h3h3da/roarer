# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.db import models
# from django import forms
from captcha.fields import CaptchaField

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nick_name = models.CharField(max_length=50, blank=True)

    class Meta(AbstractUser.Meta):
        pass