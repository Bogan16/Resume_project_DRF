# Generated by Django 4.2.3 on 2023-09-11 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0004_reservemail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ReservEmail',
        ),
    ]
