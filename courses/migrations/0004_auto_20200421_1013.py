# Generated by Django 2.2.12 on 2020-04-21 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20200421_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='abbreviation',
            field=models.CharField(default='', max_length=40),
        ),
    ]
