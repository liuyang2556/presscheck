# Generated by Django 3.0 on 2021-06-11 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checksheet', '0015_auto_20210611_1236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='updatesheet',
            old_name='加工日',
            new_name='manage_spec1',
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='manage_spec2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='manage_spec3',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='manage_spec4',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='manage_spec5',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='manage_spec6',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='manage_spec7',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='中检时间',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='中检生产数',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='二次确认1',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='二次确认2',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='二次确认3',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='初检时间',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='管理项目11',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='管理项目12',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='管理项目13',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='管理项目14',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='管理项目21',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='管理项目22',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='管理项目23',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='管理项目24',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='管理项目31',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='管理项目32',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='管理项目33',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='管理项目34',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='终检时间',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='终检生产数',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='规格值15',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='规格值16',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='规格值17',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='规格值25',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='规格值26',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='规格值27',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='规格值35',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='规格值36',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='updatesheet',
            name='规格值37',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]