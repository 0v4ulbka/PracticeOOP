# Generated by Django 5.0 on 2023-12-13 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status_comment',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Комментарий изменений'),
        ),
    ]