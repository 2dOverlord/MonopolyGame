# Generated by Django 3.2.5 on 2021-08-11 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0002_customuser_email_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='email_verified',
        ),
    ]