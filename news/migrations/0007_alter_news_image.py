# Generated by Django 3.2.9 on 2022-05-19 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20220519_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
    ]
