# Generated by Django 2.1 on 2018-10-28 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customdict', '0002_auto_20181028_1604'),
        ('loginapp', '0002_auto_20180917_2021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personaldict',
            name='user',
        ),
        migrations.DeleteModel(
            name='PersonalDict',
        ),
    ]