# Generated by Django 4.2.4 on 2023-08-17 06:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('title', models.CharField(max_length=30)),
                ('slug', models.SlugField(blank=True, max_length=30, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('title', models.CharField(max_length=30)),
                ('slug', models.SlugField(blank=True, max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('title', models.CharField(max_length=30, verbose_name='Заголовок')),
                ('slug', models.SlugField(blank=True, max_length=30, primary_key=True, serialize=False)),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='posts/', verbose_name='Картинка')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='post.category', verbose_name='Категория')),
                ('tags', models.ManyToManyField(blank=True, related_name='posts', to='post.tag')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
