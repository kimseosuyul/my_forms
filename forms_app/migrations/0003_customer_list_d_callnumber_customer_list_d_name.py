# Generated by Django 4.2.14 on 2024-09-23 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms_app', '0002_customer_list_address_customer_list_detail_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_list',
            name='d_callNumber',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='customer_list',
            name='d_name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]