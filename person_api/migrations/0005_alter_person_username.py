# Generated by Django 3.2.16 on 2023-01-24 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person_api', '0004_alter_person_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='username',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]
