from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, id, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        id = self.model.normalize_id(id)

        user = self.model(
            id=id,
            email=email,
            **extra_fields
        )
        user.set_password(password)

        # userを保存
        user.save(using=self._db)

        return user

    def create_user(self, id, email, password, **extra_fields):
        # is_staff, is_superuerが引数になければ値をFalseにして追加
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(id, email, password, **extra_fields)

    def create_superuser(self, id, email, password, **extra_fields):
        # is_staff, is_superuerが引数になければ値をTrueにして追加
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(id, email, password, **extra_fields)
