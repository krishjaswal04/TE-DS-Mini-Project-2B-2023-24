# Generated by Django 5.0.4 on 2024-04-11 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AQI', '0004_location_co_location_no2_location_o3_location_pm10_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='location_images'),
        ),
    ]
