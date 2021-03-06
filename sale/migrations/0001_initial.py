# Generated by Django 2.0.6 on 2018-06-26 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=24, verbose_name='类名')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Commdity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commdity_code', models.CharField(max_length=8, verbose_name='商品编号')),
                ('commdity_name', models.CharField(max_length=64, verbose_name='商品名称')),
                ('commdity_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='单价')),
                ('commdity_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.Category', verbose_name='商品分类')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
                'db_table': 'commdity',
            },
        ),
        migrations.CreateModel(
            name='Mod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mod_name', models.CharField(max_length=64, verbose_name='规格')),
                ('mod_gram', models.CharField(max_length=4, verbose_name='单位')),
            ],
            options={
                'verbose_name': '规格',
                'verbose_name_plural': '规格',
                'db_table': 'mod',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_name', models.CharField(max_length=64, verbose_name='店名')),
                ('position_phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='电话')),
                ('position_manager', models.CharField(blank=True, max_length=16, null=True, verbose_name='店长')),
            ],
            options={
                'verbose_name': '门店',
                'verbose_name_plural': '门店',
                'db_table': 'position',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_patch', models.CharField(max_length=14, verbose_name='批号')),
                ('stock_product', models.DateField(verbose_name='生产日期')),
                ('stock_validity', models.DateField(verbose_name='有效日期')),
                ('stock_number', models.SmallIntegerField(default=0, verbose_name='数量')),
                ('stock_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.Commdity', verbose_name='商品')),
            ],
            options={
                'verbose_name': '库存',
                'verbose_name_plural': '库存',
                'db_table': 'stock',
            },
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfer_patch', models.CharField(max_length=14, verbose_name='批号')),
                ('transfer_product', models.DateField(verbose_name='生产日期')),
                ('transfer_validity', models.DateField(verbose_name='有效日期')),
                ('transfer_number', models.PositiveSmallIntegerField(default=1, verbose_name='数量')),
                ('transfer_off', models.DecimalField(decimal_places=2, default=1, max_digits=3, verbose_name='折扣')),
                ('transfer_status', models.CharField(choices=[('1000', '销售'), ('0001', '入库'), ('1100', '调入'), ('0011', '调出')], default='1000', max_length=4, verbose_name='分类')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='操作时间')),
                ('transfer_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.Commdity', verbose_name='商品')),
                ('transfer_position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sale.Position', verbose_name='门店')),
            ],
            options={
                'verbose_name': '进销',
                'verbose_name_plural': '进销',
                'db_table': 'transfer',
            },
        ),
        migrations.AddField(
            model_name='commdity',
            name='commdity_mod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.Mod', verbose_name='规格型号'),
        ),
    ]
