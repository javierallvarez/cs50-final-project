# Generated by Django 3.2.9 on 2022-05-19 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_alter_news_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='Topic',
            new_name='topic',
        ),
    ]