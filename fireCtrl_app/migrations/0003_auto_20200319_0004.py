# Generated by Django 3.0.4 on 2020-03-18 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fireCtrl_app', '0002_auto_20200318_1337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='month',
            old_name='name',
            new_name='navn',
        ),
        migrations.RemoveField(
            model_name='month',
            name='sorting_number',
        ),
    ]
