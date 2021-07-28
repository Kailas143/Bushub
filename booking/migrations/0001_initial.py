# Generated by Django 3.2.5 on 2021-07-27 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=150)),
                ('userid', models.IntegerField()),
                ('busid', models.IntegerField()),
                ('bus_name', models.CharField(max_length=150)),
                ('source', models.CharField(max_length=150)),
                ('dest', models.CharField(max_length=150)),
                ('nos', models.PositiveIntegerField()),
                ('price', models.FloatField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.CharField(choices=[('B', 'BOOKED'), ('C', 'CANCELLED')], default='B', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Bookings',
            },
        ),
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_name', models.CharField(max_length=150)),
                ('src', models.CharField(max_length=150)),
                ('dest', models.CharField(max_length=150)),
                ('nos', models.IntegerField()),
                ('rems', models.IntegerField()),
                ('price', models.FloatField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
            options={
                'verbose_name_plural': 'Buses',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=10, unique=True)),
            ],
        ),
    ]