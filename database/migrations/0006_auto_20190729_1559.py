# Generated by Django 2.2.3 on 2019-07-29 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_auto_20190729_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='odinaryusesr',
            name='create_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='odinaryusesr',
            name='update_at',
            field=models.DateTimeField(null=True),
        ),
    ]
