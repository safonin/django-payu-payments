# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 22:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payu', '0002_auto_20160313_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payu_order_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='PayU order ID'),
        ),
    ]