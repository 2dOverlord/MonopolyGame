# Generated by Django 3.1.7 on 2021-07-30 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, default='images/DefaultProfilePicture.png', null=True, upload_to='images/'),
        ),
    ]