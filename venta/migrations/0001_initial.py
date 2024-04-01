# Generated by Django 4.2.11 on 2024-03-30 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('identificacion', models.IntegerField(null=True)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254, null=True)),
                ('address', models.CharField(max_length=100)),
                ('municipio', models.CharField(max_length=100)),
                ('departamento', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
                'db_table': 'customer',
                'managed': True,
            },
        ),
    ]
