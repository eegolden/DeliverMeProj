# Generated by Django 3.0.5 on 2020-04-27 15:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickupName', models.CharField(max_length=30)),
                ('pickupStreetAddress', models.CharField(max_length=100)),
                ('pickupCity', models.CharField(max_length=20)),
                ('pickupState', models.CharField(max_length=2)),
                ('pickupZipcode', models.CharField(max_length=5)),
                ('dropoffName', models.CharField(max_length=30)),
                ('dropoffStreetAddress', models.CharField(max_length=100)),
                ('dropoffCity', models.CharField(max_length=20)),
                ('dropoffState', models.CharField(max_length=2)),
                ('dropoffZipcode', models.CharField(max_length=5)),
                ('item', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('dateCreated', models.DateTimeField(default=django.utils.timezone.now)),
                ('lastModified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
