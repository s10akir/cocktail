from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):
    def _create_user(self, user_id, email, password, **extra_fields):
        # emailの確認
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user_id = self.model.normalize_user_id(user_id)

        # 項目をuserに入れる
        user = self.model(
            user_id = user_id,
            email = email,
            **extra_fields
        )
        user.set_password(password)

        # userを保存 
        user.save(using = self._db)

        return user

    def create_user(self, user_id, email, password, **extra_fields):
        # 一般ユーザーか確認
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        
        return self._create_user(user_id, email, password, **extra_fields)

    def create_superuser(self, user_id, email, password, **extra_fields):
        # スーパーユーザーか確認
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(user_id, email, password, **extra_fields)