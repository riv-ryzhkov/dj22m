# Generated by Django 4.2.7 on 2023-11-09 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=50, verbose_name='Назва'),
        ),
    ]
