# Generated by Django 4.2.1 on 2023-05-25 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('general_title', models.CharField(max_length=50, verbose_name='General Title')),
                ('img', models.ImageField(upload_to='images', verbose_name='Logo Image')),
                ('path1', models.CharField(max_length=50, verbose_name='Path 1')),
                ('path2', models.CharField(max_length=50, verbose_name='Path 2')),
                ('path3', models.CharField(max_length=50, verbose_name='Path 3')),
                ('path4', models.CharField(max_length=50, verbose_name='Path 4')),
                ('path5', models.CharField(max_length=50, verbose_name='Path 5')),
                ('path6', models.CharField(max_length=50, verbose_name='Path 6')),
                ('path7', models.CharField(max_length=50, verbose_name='Path 7')),
            ],
            options={
                'verbose_name': 'Header',
                'verbose_name_plural': 'Header',
            },
        ),
    ]
