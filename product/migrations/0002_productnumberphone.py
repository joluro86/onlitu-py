# Generated by Django 5.0.3 on 2024-04-03 16:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductNumberPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.BigIntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.producto')),
            ],
            options={
                'verbose_name': 'product_number_phone',
                'verbose_name_plural': 'product_number_phone',
                'db_table': 'product_number_phone',
                'managed': True,
            },
        ),
    ]
