# Generated by Django 3.2 on 2021-07-13 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UserApp', '0001_initial'),
        ('ItemApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.customuser'),
        ),
    ]
