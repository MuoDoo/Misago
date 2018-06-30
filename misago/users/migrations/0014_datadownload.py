# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-24 00:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import misago.users.models.datadownload


class Migration(migrations.Migration):

    dependencies = [
        ('misago_users', '0013_auto_20180609_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataDownload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveIntegerField(choices=[(0, 'Pending'), (1, 'Processing'), (2, 'Ready'), (3, 'Expired')], db_index=True, default=0)),
                ('requester_name', models.CharField(max_length=255)),
                ('requested_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('expires_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('file', models.FileField(blank=True, max_length=255, null=True, upload_to=misago.users.models.datadownload.get_data_upload_to)),
                ('requester', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
    ]
