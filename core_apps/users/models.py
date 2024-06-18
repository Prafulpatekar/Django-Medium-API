import uuid

from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

class User(AbstractBaseUser,PermissionsMixin):
    # pseudo primary key to avoid disadvantage of uuid primary key
    pkid = models.BigAutoField(primary_key=True,editable=False) 
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    first_name = models.CharField(verbose_name=("first name"),max_length=50)
    last_name = models.CharField(verbose_name=("last name"),max_length=50)
    email = models.EmailField(verbose_name=("email address"),db_index=True,unique=True) # db_index to create indexing for email field
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ["first_name","last_name"]

    objects = CustomUserManager()
    
    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self) -> str:
        return f"{self.first_name}"
    
    @property
    def get_full_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}" 
    
    @property
    def get_short_name(self):
        return self.first_name






