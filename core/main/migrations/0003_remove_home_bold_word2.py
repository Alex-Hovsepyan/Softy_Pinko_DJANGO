# Generated by Django 4.2.1 on 2023-05-25 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_home_homecontent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='bold_word2',
        ),
    ]