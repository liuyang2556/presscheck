# Generated by Django 3.0 on 2021-06-13 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checksheet', '0018_auto_20210613_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='updatesheet',
            name='确认点位',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
