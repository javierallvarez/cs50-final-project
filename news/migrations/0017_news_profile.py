# Generated by Django 3.2.9 on 2022-05-23 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_auto_20220522_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='profile',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_posts', to='news.profile'),
        ),
    ]