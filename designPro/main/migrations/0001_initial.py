# Generated by Django 5.0 on 2023-12-13 08:18

import django.contrib.auth.models
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import main.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=254, verbose_name='Имя')),
                ('surname', models.CharField(max_length=254, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=254, verbose_name='Отчество')),
                ('username', models.CharField(max_length=254, unique=True, verbose_name='Логин')),
                ('email', models.CharField(max_length=254, unique=True, verbose_name='Почта')),
                ('password', models.CharField(max_length=254, verbose_name='Пароль')),
                ('role', models.CharField(choices=[('admin', 'Администратор'), ('user', 'Пользователь')], default='user', max_length=254, verbose_name='Роль')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='Имя')),
                ('description', models.CharField(max_length=500, verbose_name='Описание')),
                ('photo_file', models.ImageField(blank=True, max_length=254, null=True, upload_to=main.models.get_name_file, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('status', models.CharField(blank=True, choices=[('', 'Новая'), ('', 'Принято в работу'), ('', 'Выполнено')], default='', max_length=1, verbose_name='Дата добавления')),
                ('status_comment', models.CharField(blank=True, max_length=500, null=True, verbose_name='Описание')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='Категория')),
            ],
        ),
    ]
