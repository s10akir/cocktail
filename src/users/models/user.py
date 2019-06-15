import uuid

from django.db import models
from django.contrib.auth.models import PermissionMixin
from django.contrib.auth.base_user import AbstractBaseUser


class User(AbstractBaseUser, PermissionMixin):
    # 代理キー（UUIDで実現）
    id = models.UUIDField(primary_key=True, default=uuid.4,
                               editable=false)
    # アカウント作成日（DBにINSERTしたときで判断）
    created_at = models.DataTimeField(auto_now_add=True)
    update_at = models.DataTimeField(auto_now=True)
    # とりあえず20文字
    password = models.CharField(max_length=20)
    before_password = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, unique=True)
    # 組織名または個人名
    name = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # 標準のBaseUserManagerを使う代わりにUserManagerを使うことを明示
    objects = UserManager()

    # ユーザのユニークなキーを設定
    USERNAME_FIELD = 'id'
    # ユーザモデルのEメールフィールドの設定
    EMAIL_FIELD = 'email'
    # 入力必須項目。USERNAME_FIELDとpasswordは書かなくてよい（常に必要なため）
    REQUIRED_FIELDS = ['email']