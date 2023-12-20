from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django import forms

from .models import User, Application, Category


class RegisterUserForm(forms.ModelForm):
    email = forms.EmailField(required=True,
                             label='Адрес электронной почты')
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput,
                               help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Пароль (повторно)',
                                widget=forms.PasswordInput,
                                help_text='Повторите тот же самый пароль еще раз')

    def clean(self):
        super().clean()
        password = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            errors = {'password2': ValidationError(
                'Введенные пароли не совпадают', code='password_mismatch'
            )}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return super(RegisterUserForm, self).save(user)

    class Meta:
        model = User
        fields = ('name', 'surname', 'patronymic', 'username', 'email', 'password', 'password2',)


class AddApplication(forms.ModelForm):
    name = forms.CharField(required=True, label='Название')
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}), label='Описание')
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Категория не выбрана',
                                      label='Категория')

    # save(self, commit=True):
    # application = super().save(commit=False)
    # if commit:
    # application.save()
    # return super(AddApplication, self).save(application)

    class Meta:
        model = Application
        fields = ('user', 'name', 'description', 'category')
        widgets = {'user': forms.HiddenInput}
