# Generated by Django 4.2.1 on 2023-05-25 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_home_options_alter_homecontent_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='bold_word1',
            field=models.CharField(max_length=30, verbose_name='Bold Part'),
        ),
        migrations.AlterField(
            model_name='home',
            name='subtitle',
            field=models.TextField(max_length=100, verbose_name='SubTitle'),
        ),
        migrations.AlterField(
            model_name='homecontent',
            name='subtitle',
            field=models.CharField(max_length=60, verbose_name='Subtitle'),
        ),
    ]
