import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from user.models.user_manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    # 代理キー（UUIDで実現）
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False)
    # アカウント作成日（DBにINSERTしたときで判断）
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=256)
    before_password = models.CharField(max_length=256)
    email = models.EmailField(max_length=254, unique=True)
    # 組織名または個人名
    name = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # 標準のBaseUserManagerを使う代わりにUserManagerを使うことを明示
    objects = UserManager()

    # ユーザのユニークなキーを設定（ログイン時に使用されるID的なもの）
    USERNAME_FIELD = 'email'
    # ユーザモデルのEメールフィールドの設定
    EMAIL_FIELD = 'email'
    # 入力必須項目。USERNAME_FIELDとpasswordは書かなくてよい（常に必要なため）
    REQUIRED_FIELDS = []

    def set_before_password(self, raw_password):
        self.before_password = make_password(raw_password)

    def update_email(self, email):
        self.email = email
        self.save()

    def update_name(self, name):
        self.name = name
        self.save()
