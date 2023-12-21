from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django import forms
from django.core.validators import RegexValidator

from .models import User, Application, Category


class RegisterUserForm(forms.ModelForm):
    name = forms.CharField(label='Имя', validators=[RegexValidator('^[а-яА-Я- ]+$',
                                                                   message='Разрешены только кириллические '
                                                                           'буквы, дефис и пробелы')],
                           error_messages={'required': 'Обязательное поле'})
    surname = forms.CharField(label='Фамилия', validators=[RegexValidator('^[а-яА-Я- ]+$',
                                                                          message='Разрешены только кириллические '
                                                                                  'буквы, дефис и пробелы')],
                              error_messages={'required': 'Обязательное поле'})
    patronymic = forms.CharField(label='Отчество', required=False, validators=[RegexValidator('^[а-яА-Я- ]+$',
                                                                                              message='Разрешены только кириллические '
                                                                                                      'буквы, дефис и пробелы')])
    username = forms.CharField(label='Логин', validators=[RegexValidator('^[a-zA-Z-]+$',
                                                                         message='Разрешены только латиница и дефис')],
                               error_messages={
                                   'required': 'Обязательное поле',
                                   'unique': 'Данный логин уже занят'
                               })
    email = forms.EmailField(required=True,
                             label='Адрес электронной почты',
                             error_messages={
                                 'invalid': 'Не правильный формат',
                                 'unique': 'Данный почтовый адресс уже занят'
                             })
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput,
                               error_messages={'required': 'Обязательное поле'})
    password2 = forms.CharField(label='Пароль (повторно)',
                                widget=forms.PasswordInput,
                                help_text='Повторите тот же самый пароль еще раз',
                                error_messages={'required': 'Обязательное поле'})

    def clean(self):
        super().clean()
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise ValidationError({
                'password2': ValidationError('Пароли не совпадают', code='password_nisnatch')
            })

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('name', 'surname', 'patronymic', 'username', 'email', 'password', 'password2',)


class AddApplication(forms.ModelForm):
    name = forms.CharField(required=True, label='Название')
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}), label='Описание')
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Категория не выбрана',
                                      label='Категория')

    class Meta:
        model = Application
        fields = ('user', 'name', 'description', 'category', 'photo_file')
        widgets = {'user': forms.HiddenInput}


class AddCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class ApplicationUpdateD(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('status', 'photo_file')
        widgets = {'status': forms.HiddenInput}


class ApplicationUpdateP(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('status', 'status_comment')
        widgets = {
            'status': forms.HiddenInput,
        }
