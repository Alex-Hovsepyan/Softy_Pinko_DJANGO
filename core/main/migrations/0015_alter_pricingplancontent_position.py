# Generated by Django 4.2.1 on 2023-05-25 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_pricingplanoffer_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricingplancontent',
            name='position',
            field=models.CharField(max_length=50, verbose_name='Top Or Bottom'),
        ),
    ]