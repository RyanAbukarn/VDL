# Generated by Django 4.0.6 on 2022-07-10 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='file',
            field=models.FileField(default='', upload_to='documents/'),
        ),
    ]
