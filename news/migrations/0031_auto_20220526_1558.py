# Generated by Django 3.2.9 on 2022-05-26 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0030_auto_20220526_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='readlist',
            name='newslist',
        ),
        migrations.AddField(
            model_name='readlist',
            name='news',
            field=models.ManyToManyField(blank=True, related_name='news_readlist', to='news.News'),
        ),
    ]
