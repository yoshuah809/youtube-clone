# Generated by Django 3.2.9 on 2021-11-10 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='commentDislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='commentLikes',
            field=models.IntegerField(default=0),
        ),
    ]
