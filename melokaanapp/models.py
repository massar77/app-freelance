from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from .utils import unique_slug_generator
from django.db.models.signals import pre_save

User = get_user_model()

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.designation, instance.slug)


class Category_1(models.Model):
    designation = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, blank=True)
    photo_main = models.ImageField(upload_to='photo/%Y/%m/', null=True, blank=True)
    icon = models.ImageField(upload_to='icon/%Y/%m/', null=True, blank=True)

    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    add = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.designation
pre_save.connect(slug_generator, sender=Category_1)

class Category_2(models.Model):
    designation = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, blank=True)
    photo_main = models.ImageField(upload_to='photo/%Y/%m/', null=True, blank=True)
    icon = models.ImageField(upload_to='icon/%Y/%m/', null=True, blank=True)
    category_1 = models.ForeignKey(Category_1, on_delete=models.DO_NOTHING, null=True, blank=True)

    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    add = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.designation
pre_save.connect(slug_generator, sender=Category_2)

class Post(models.Model):
    designation = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=250, blank=True)
    description = models.TextField(blank=True)
    price = models.IntegerField(null=True, blank=True)
    first_price = models.IntegerField(blank=True, null=True)
    last_price = models.IntegerField(null=True, blank=True)

    photo_main = models.ImageField(upload_to='photo/%Y/%m/', null=True, blank=True)
    photo_1 = models.ImageField(upload_to='photo/%Y/%m/', null=True, blank=True)
    photo_2 = models.ImageField(upload_to='photo/%Y/%m/', null=True, blank=True)
    photo_3 = models.ImageField(upload_to='photo/%Y/%m/', null=True, blank=True)
    photo_4 = models.ImageField(upload_to='photo/%Y/%m/', null=True, blank=True)
    photo_5 = models.ImageField(upload_to='photo/%Y/%m/', null=True, blank=True)
    photo_6 = models.ImageField(upload_to='photo/%Y/%m/', null=True, blank=True)
    
    is_published = models.BooleanField(default=True)
    
    category_1 = models.ForeignKey(Category_1, on_delete=models.DO_NOTHING, null=True, blank=True)
    category_2 = models.ForeignKey(Category_2, on_delete=models.DO_NOTHING, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    add = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.designation
pre_save.connect(slug_generator, sender=Post)


class Offer(models.Model):
    price = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)

    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    add = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user', null=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE,related_name='client', null=True)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    add = models.DateTimeField(auto_now_add=True, null=True, blank=True)