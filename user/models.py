from django.db import models

from  django.contrib.auth.models import (
    BaseUserManager,AbstractBaseUser
)

class UserManager(BaseUserManager):
    def create_user(self,email,first_name,last_name,password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user=self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,first_name,last_name,password=None):
        user=self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user
        
class User(AbstractBaseUser):
    email=models.CharField( verbose_name='email address', max_length=255,unique=True,)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    is_staff =models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']

    class Meta:
        db_table = 'user'

    

    def __str__(self) -> str:
        return self.email
    
    def has_perm(self, perm,obj=None):
        return True
    
    def has_module_perms(self,app_label):
        return True


