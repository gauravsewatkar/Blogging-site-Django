# Generated by Django 3.2 on 2021-06-18 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogcomment_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomment',
            name='views',
        ),
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]