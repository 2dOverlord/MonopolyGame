# Generated by Django 3.1.7 on 2021-07-30 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0003_auto_20210730_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, default='images/ProfilePicture.png', null=True, upload_to='images/'),
        ),
    ]
