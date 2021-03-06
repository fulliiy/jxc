# Generated by Django 2.0.6 on 2018-06-26 10:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sale', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(max_length=48, verbose_name='活动')),
                ('activity_content', models.TextField(verbose_name='活动内容')),
                ('start_date', models.DateTimeField(verbose_name='开始时间')),
                ('end_date', models.DateTimeField(verbose_name='结束时间')),
            ],
            options={
                'verbose_name': '活动列表',
                'verbose_name_plural': '活动列表',
                'db_table': 'activity',
            },
        ),
        migrations.CreateModel(
            name='Subhead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subhead_affair', models.CharField(max_length=128, verbose_name='事务')),
                ('max_date', models.DateField(verbose_name='日期上限')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('subhead_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '事务交接',
                'verbose_name_plural': '事务交接',
                'db_table': 'subhead',
            },
        ),
    ]
