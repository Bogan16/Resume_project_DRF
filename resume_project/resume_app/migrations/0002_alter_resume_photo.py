# Generated by Django 4.2.3 on 2023-09-11 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='photo',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]