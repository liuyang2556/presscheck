# Generated by Django 3.0 on 2021-06-11 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checksheet', '0013_auto_20210611_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='updatesheet',
            name='BL材批次号1',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='BL材批次号2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='BL材生产日期1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='BL材生产日期2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='使用冲床',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='设变号',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]