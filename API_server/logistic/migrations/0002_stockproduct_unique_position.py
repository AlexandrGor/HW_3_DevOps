# Generated by Django 4.0.1 on 2022-04-06 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='stockproduct',
            constraint=models.UniqueConstraint(fields=('stock', 'product'), name='unique_position'),
        ),
    ]
