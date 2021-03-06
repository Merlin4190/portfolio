# Generated by Django 3.0.8 on 2020-08-02 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_portfolio', '0003_auto_20200728_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(default=None, upload_to='images/portfolio'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default=None, upload_to='images/avatar'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='facebook_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='instagram_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='linkedin_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pininterest_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twitter_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='youtube_url',
            field=models.URLField(blank=True),
        ),
    ]
