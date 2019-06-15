import uuid

from django.db import models
from django.contrib.auth.models import PermissionMixin
from django.contrib.auth.base_user import AbstractBaseUser


class User(AbstractBaseUser, PermissionMixin):
    # 代理キー（UUIDで実現）
    user_id = models.UUIDField(primary_key=True, default=uuid.4,
                               editable=false)
    # アカウント作成日（DBにINSERTしたとき）
    created_at = models.DataTimeField(auto_now_add=True)
    # アカウント更新日（更新がかかったとき）
    update_at = models.DataTimeField(auto_now=True)
    # パスワード（とりあえず20文字）
    password = models.CharField(max_length=20)
    # 前回パスワード
    before_password = models.CharField(max_length=20)
    # メールアドレス
    email = models.EmailField(max_length=254)
    # 組織名または個人名
    name = models.CharField(max_length=50)
    # 管理者サイトにTrueならいける
    is_staff = models.BooleanField(default=False)
    # アクティブかどうか
    is_active = models.BooleanField(default=True)

    # 標準のBaseUserManagerを使う代わりにUserManagerを使うことを明示
    objects = UserManager()

    # ユーザのユニークなキー
    USERNAME_FIELD = 'user_id'
    # ユーザモデルのEメールフィールド
    EMAIL_FIELD = 'email'
    # 入力必須項目。USERNAME_FIELDとpasswordは書かなくてよい（常に必要なため）
    REQUIRED_FIELDS = ['email']