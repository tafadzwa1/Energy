# Generated by Django 3.2.6 on 2021-09-01 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='FonNumber',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
