# Generated by Django 2.0.6 on 2018-06-29 01:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0012_remove_transfer_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='操作时间'),
            preserve_default=False,
        ),
    ]
