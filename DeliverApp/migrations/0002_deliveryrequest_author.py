# Generated by Django 3.0.5 on 2020-04-26 19:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('DeliverApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryrequest',
            name='author',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
