# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 12:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('literature', '0002_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorBookThrough',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='literature.Author')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='literature.Book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='books_m2m', through='literature.AuthorBookThrough', to='literature.Author'),
        ),
        migrations.AlterUniqueTogether(
            name='authorbookthrough',
            unique_together=set([('author', 'book')]),
        ),
    ]