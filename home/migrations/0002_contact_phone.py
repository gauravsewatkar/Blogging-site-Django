# Generated by Django 3.2 on 2021-06-13 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default=1, max_length=13),
            preserve_default=False,
        ),
    ]