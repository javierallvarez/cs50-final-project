# Generated by Django 3.2.9 on 2022-05-26 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0031_auto_20220526_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='readlist',
            field=models.ManyToManyField(blank=True, related_name='news_readlist', to='news.Comment'),
        ),
        migrations.DeleteModel(
            name='Readlist',
        ),
    ]
