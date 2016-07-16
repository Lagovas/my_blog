# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-16 12:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=200)),
                ('article_text', models.TextField()),
                ('article_date', models.DateTimeField()),
                ('article_likes', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments_date', models.DateTimeField(blank=True, null=True)),
                ('comments_text', models.TextField(verbose_name='Comments text')),
                ('comments_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Article')),
                ('comments_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'comments',
            },
        ),
    ]