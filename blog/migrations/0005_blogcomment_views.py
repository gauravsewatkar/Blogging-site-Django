# Generated by Django 3.2 on 2021-06-18 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210616_0700'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
