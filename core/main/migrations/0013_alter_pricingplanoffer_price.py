# Generated by Django 4.2.1 on 2023-05-25 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_pricingplanoffer_offer1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricingplanoffer',
            name='price',
            field=models.FloatField(verbose_name='Price'),
        ),
    ]
