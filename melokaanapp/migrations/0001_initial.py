# Generated by Django 3.2.9 on 2021-11-18 13:13

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=250)),
                ('slug', models.SlugField(blank=True, max_length=250)),
                ('photo_main', models.ImageField(blank=True, null=True, upload_to='photo/%Y/%m/')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='icon/%Y/%m/')),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('add', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=250)),
                ('slug', models.SlugField(blank=True, max_length=250)),
                ('photo_main', models.ImageField(blank=True, null=True, upload_to='photo/%Y/%m/')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='icon/%Y/%m/')),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('add', models.DateTimeField(auto_now_add=True, null=True)),
                ('category_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='melokaanapp.category_1')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('add', models.DateTimeField(auto_now_add=True, null=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(blank=True, max_length=250)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('first_price', models.IntegerField(blank=True, null=True)),
                ('last_price', models.IntegerField(blank=True, null=True)),
                ('photo_main', models.ImageField(blank=True, null=True, upload_to='photo/%Y/%m/')),
                ('photo_1', models.ImageField(blank=True, null=True, upload_to='photo/%Y/%m/')),
                ('photo_2', models.ImageField(blank=True, null=True, upload_to='photo/%Y/%m/')),
                ('photo_3', models.ImageField(blank=True, null=True, upload_to='photo/%Y/%m/')),
                ('photo_4', models.ImageField(blank=True, null=True, upload_to='photo/%Y/%m/')),
                ('photo_5', models.ImageField(blank=True, null=True, upload_to='photo/%Y/%m/')),
                ('photo_6', models.ImageField(blank=True, null=True, upload_to='photo/%Y/%m/')),
                ('is_published', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('add', models.DateTimeField(auto_now_add=True, null=True)),
                ('category_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='melokaanapp.category_1')),
                ('category_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='melokaanapp.category_2')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('add', models.DateTimeField(auto_now_add=True, null=True)),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='melokaanapp.post')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
