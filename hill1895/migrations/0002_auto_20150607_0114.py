# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hill1895', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='head_pic_url',
            field=models.CharField(default=b'/static/img/default.jpg', max_length=250, verbose_name='\u5934\u56fe\u94fe\u63a5'),
        ),
    ]
