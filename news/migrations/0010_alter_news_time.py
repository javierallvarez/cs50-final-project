# Generated by Django 3.2.9 on 2022-05-19 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20220519_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='time',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
    ]
