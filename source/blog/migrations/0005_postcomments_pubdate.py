# Generated by Django 2.0.5 on 2018-07-08 10:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_postcomments'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcomments',
            name='pubDate',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 8, 12, 36, 8, 845602)),
        ),
    ]
