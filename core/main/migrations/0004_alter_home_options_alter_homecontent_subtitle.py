# Generated by Django 4.2.1 on 2023-05-25 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_home_bold_word2'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='home',
            options={'verbose_name': 'Home', 'verbose_name_plural': 'Home'},
        ),
        migrations.AlterField(
            model_name='homecontent',
            name='subtitle',
            field=models.TextField(verbose_name='Subtitle'),
        ),
    ]