from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

MESSAGE_NO_EMAIL = "Veuillez saisir un mail !"
MESSAGE_NO_PSEUDO = "Veuillez saisir un pseudo !"
# Create your models here.

class MysUserManager(BaseUserManager):
    def create_user(self, pseudo, email, password=None):
        if not pseudo:
            raise ValueError(MESSAGE_NO_PSEUDO)

        if not email:
            raise ValueError(MESSAGE_NO_EMAIL)

        user = self.model(
            pseudo=pseudo,
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, pseudo, email, password=None):
        user = self.create_user(pseudo=pseudo, email=email, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user

class ConnectUser(AbstractBaseUser):
    pseudo = models.CharField(
        unique=True,
        max_length=10,
        blank=False
    )
    email = models.EmailField(
        unique=True,
        max_length=255,
        blank=False
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "pseudo"
    REQUIRED_FIELDS = ["email"]
    objects = MysUserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True