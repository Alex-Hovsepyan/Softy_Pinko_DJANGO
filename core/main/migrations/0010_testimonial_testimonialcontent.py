# Generated by Django 4.2.1 on 2023-05-25 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_workproces_workprocesscontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
            ],
        ),
        migrations.CreateModel(
            name='TestimonialContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(upload_to='images', verbose_name='Image 1')),
                ('text', models.TextField(verbose_name='Text')),
                ('img2', models.ImageField(upload_to='images', verbose_name='Image 2')),
                ('name', models.CharField(max_length=60, verbose_name='Name')),
                ('profession', models.CharField(max_length=80, verbose_name='Profession')),
            ],
        ),
    ]
