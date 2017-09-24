# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0018_auto_20170924_0609'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='coming',
            field=models.BooleanField(default=False, help_text='Indicates whether users are coming from an old feed; if set, leave for four weeks; see <a href="https://help.apple.com/itc/podcasts_connect/#/itca489031e0">documentation</a>', verbose_name='coming'),
        ),
        migrations.AddField(
            model_name='show',
            name='going',
            field=models.URLField(blank=True, help_text='Permanently redirect users to URL of a new feed; see <a href="https://help.apple.com/itc/podcasts_connect/#/itca489031e0">documentation</a>', verbose_name='going'),
        ),
    ]
