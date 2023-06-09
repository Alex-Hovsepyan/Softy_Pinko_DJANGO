# Generated by Django 4.2.1 on 2023-05-25 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_contactget'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, verbose_name='Username')),
                ('user_email', models.EmailField(max_length=254, verbose_name='User Email')),
                ('user_message', models.TextField(verbose_name='User Message')),
            ],
            options={
                'verbose_name': 'Contact POST',
                'verbose_name_plural': 'Contact POST',
            },
        ),
    ]
