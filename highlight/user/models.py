from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email = None, password = None):
        user = self.model(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, email):
        user = self.create_user(
            password=password,
            username=username,
            email=email,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPE=(
        ('customer', 'Customer'),
        ('editor', 'Editor'),
    )

    username = models.CharField(
        max_length=8,
        blank=False,
        unique=True
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE,
    )
    name = models.CharField(
        max_length=30,
    )
    phone_number=models.CharField(
        max_length=12,        
    )
    
    is_active = models.BooleanField(default=True)
    is_admin= models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'user',
        verbose_name_plural = 'users'

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_superuser
    
    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']
    object = CustomUserManager()