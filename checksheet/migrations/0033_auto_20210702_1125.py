# Generated by Django 3.0 on 2021-07-02 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checksheet', '0032_remove_updatesheet_模具检查清扫'),
    ]

    operations = [
        migrations.AddField(
            model_name='updatesheet',
            name='加工批次号',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='模具检查清扫',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='计划数量',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]