from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.conf import settings

class UserManager(BaseUserManager):
    def _create_user(self,  email, name, password, is_staff, is_superuser,  **extra_fields):
        email = self.normalize_email(email)
        user = self.model(
            email = email,
            name = name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, name, password=None, **extra_fields):
        return self._create_user( email, name, password, False, False **extra_fields)


    def create_superuser(self, email, name, password=None, **extra_fields):
        return self._create_user( email, name, password, True, True,  **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
      
    ruc = models.CharField('ruc', max_length=11, unique = True, null = True, blank = True )
    email = models.EmailField('email',max_length = 255, unique = True,)
    email_verify = models.BooleanField( 'verificacion', default= False )
    name = models.CharField('Nombres', max_length = 255, blank = False, null = False)
    phone = models.CharField('celular', max_length=9,  null = True, blank = True )
    api_token = models.TextField('token', blank = True, null = True )
    api_token_email = models.TextField('token email', blank = True, null = True )
    hold = models.CharField('sigla', max_length=10, blank = True, null = True )
    created_by = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    is_state = models.BooleanField(default = True) 
    is_staff = models.BooleanField(default = False)
    is_admin = models.BooleanField(default = False)
    objects = UserManager()

    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return f'{self.name}'


