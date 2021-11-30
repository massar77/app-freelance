from django.db import models
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.username, instance.slug)


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            # date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            # date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    # date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    username = models.CharField(max_length=300, null=True, blank=True)
    first_name = models.CharField(max_length=300, null=True, blank=True)
    last_name = models.CharField(max_length=300, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=250, blank=True)
    adress_1 = models.CharField(max_length=500,null=True, blank=True)
    adress_2 = models.CharField(max_length=500,null=True, blank=True)
    country = models.CharField(max_length=500,null=True, blank=True)
    region = models.CharField(max_length=500,null=True, blank=True)
    ville = models.CharField(max_length=500,null=True, blank=True)
    code_postal = models.CharField(max_length=500,null=True, blank=True)

    photo_main = models.ImageField(upload_to='photo_user/%Y/%m/', null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    add = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

pre_save.connect(slug_generator, sender=MyUser)
