# Generated by Django 3.2.9 on 2022-05-18 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_comments_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
    ]
