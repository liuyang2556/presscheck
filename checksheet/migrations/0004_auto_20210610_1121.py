# Generated by Django 3.0 on 2021-06-10 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checksheet', '0003_auto_20210609_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updatesheet',
            name='content_type',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
