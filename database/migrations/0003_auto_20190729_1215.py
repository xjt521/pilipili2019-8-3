# Generated by Django 2.2.3 on 2019-07-29 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20190726_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='odinaryusesr',
            name='user_email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='odinaryusesr',
            name='user_id',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
