# Generated by Django 3.0.4 on 2020-08-27 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_portfolio', '0005_auto_20200818_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('design', models.ImageField(default=None, upload_to='images/template')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='upload_cv',
            field=models.FileField(blank=True, null=True, upload_to='files/cv'),
        ),
        migrations.AddField(
            model_name='profile',
            name='template',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_template', to='my_portfolio.Template'),
        ),
    ]
