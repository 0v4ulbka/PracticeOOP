from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string


def get_name_file(instance, filename):
    return '/'.join([get_random_string(length=5) + '_' + filename])


class User(AbstractUser):
    name = models.CharField(max_length=254, verbose_name='Имя', blank=False)
    surname = models.CharField(max_length=254, verbose_name='Фамилия', blank=False)
    patronymic = models.CharField(max_length=254, verbose_name='Отчество', blank=True)
    username = models.CharField(max_length=254, verbose_name='Логин', blank=False, unique=True)
    email = models.CharField(max_length=254, verbose_name='Почта', blank=False, unique=True)
    password = models.CharField(max_length=254, verbose_name='Пароль', blank=False)
    role = models.CharField(max_length=254, verbose_name='Роль',
                            choices=(('admin', 'Администратор'), ('user', 'Пользователь')), default='user')

    USERNAME_FIELD = 'username'

    def __str__(self):
        return str(self.name) + " " + str(self.surname)


class Category(models.Model):
    name = models.CharField(max_length=254, verbose_name='Название', blank=False)

    def __str__(self):
        return self.name


class Application(models.Model):
    name = models.CharField(max_length=254, verbose_name='Имя', blank=False)
    description = models.CharField(max_length=500, verbose_name='Описание', blank=False)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    photo_file = models.ImageField(max_length=254, upload_to=get_name_file,
                                   blank=True, null=True,
                                   validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])
    date = models.DateTimeField(verbose_name='Дата добавления', auto_now_add=True)

    LOAN_STATUS = (
        ('', 'Новая'),
        ('', 'Принято в работу'),
        ('', 'Выполнено'),
    )

    status = models.CharField(max_length=1, verbose_name='Дата добавления',
                              choices=LOAN_STATUS, blank=True, default='')
    status_comment = models.CharField(max_length=500, verbose_name='Комментарий изменений', blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
