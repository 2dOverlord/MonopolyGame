# Generated by Django 3.2.5 on 2021-07-29 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=30)),
                ('item_type', models.CharField(choices=[['Player', 'PLAYER'], ['Manager', 'MANAGER'], ['Team', 'TEAM']], default='ONE', max_length=30)),
                ('rarity', models.CharField(choices=[['0', 'BASIC'], ['1', 'RARE'], ['2', 'LEGEND']], default='NOT RARE', max_length=30)),
                ('on_sale', models.BooleanField(default=False)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
