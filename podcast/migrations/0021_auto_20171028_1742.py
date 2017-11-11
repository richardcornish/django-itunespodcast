# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-28 17:42
from __future__ import unicode_literals

from django.db import migrations, models
import podcast.utils


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0020_auto_20171026_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enclosure',
            name='file',
            field=models.FileField(help_text='Supported formats: M4A, MP3, MOV, MP4, M4V, PDF, and EPUB', upload_to=podcast.utils.enclosure_file_path, verbose_name='file'),
        ),
        migrations.AlterField(
            model_name='enclosure',
            name='poster',
            field=models.ImageField(blank=True, help_text='For video files', upload_to=podcast.utils.enclosure_poster_path, verbose_name='poster'),
        ),
        migrations.AlterField(
            model_name='episode',
            name='image',
            field=models.ImageField(blank=True, help_text="1400&times;1400&ndash;3000&times;3000px, 72DPI, JPG/PNG, RGB; if blank, uses show's image", upload_to=podcast.utils.episode_image_path, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='show',
            name='image',
            field=models.ImageField(blank=True, help_text='1400&times;1400&ndash;3000&times;3000px; 72DPI; JPG, PNG; RGB; if blank, default <a href="/static/podcast/img/no_artwork.png">no artwork</a> is used', upload_to=podcast.utils.show_image_path, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='photo',
            field=models.ImageField(blank=True, upload_to=podcast.utils.speaker_photo_path, verbose_name='Photo'),
        ),
    ]