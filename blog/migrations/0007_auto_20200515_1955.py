# Generated by Django 2.2.12 on 2020-05-15 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200515_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='rating',
            field=models.IntegerField(),
        ),
    ]