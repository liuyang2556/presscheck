# Generated by Django 3.0 on 2021-06-26 09:09

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('checksheet', '0023_auto_20210624_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckSheetBL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('管理编号', models.CharField(blank=True, max_length=10, null=True)),
                ('parts_code', models.CharField(blank=True, max_length=20, null=True)),
                ('parts_name', models.CharField(blank=True, max_length=50, null=True)),
                ('标准spm', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('容器', models.CharField(blank=True, max_length=5, null=True)),
                ('SNP', models.IntegerField(blank=True, default=0, null=True)),
                ('材质', models.CharField(blank=True, max_length=20, null=True)),
                ('板厚', models.CharField(blank=True, max_length=20, null=True)),
                ('标准材料宽度', models.IntegerField(blank=True, default=0, null=True)),
                ('进给量', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('发生日1', models.DateField(blank=True, null=True)),
                ('发生日2', models.DateField(blank=True, null=True)),
                ('发生日3', models.DateField(blank=True, null=True)),
                ('不合格内容1', models.CharField(blank=True, max_length=100, null=True)),
                ('不合格内容2', models.CharField(blank=True, max_length=100, null=True)),
                ('不合格内容3', models.CharField(blank=True, max_length=100, null=True)),
                ('发生原因1', models.CharField(blank=True, max_length=100, null=True)),
                ('发生原因2', models.CharField(blank=True, max_length=100, null=True)),
                ('发生原因3', models.CharField(blank=True, max_length=100, null=True)),
                ('规格值1', models.CharField(blank=True, max_length=20, null=True)),
                ('规格值2', models.CharField(blank=True, max_length=20, null=True)),
                ('规格值3', models.CharField(blank=True, max_length=20, null=True)),
                ('规格值4', models.CharField(blank=True, max_length=20, null=True)),
                ('规格值5', models.CharField(blank=True, max_length=20, null=True)),
                ('规格值6', models.CharField(blank=True, max_length=20, null=True)),
                ('规格值7', models.CharField(blank=True, max_length=20, null=True)),
                ('content1', ckeditor_uploader.fields.RichTextUploadingField()),
                ('content2', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('last_updated_time', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('car_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='checksheet.CarType', verbose_name='car_type')),
                ('machine_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checksheet.MachineType')),
                ('确认方法1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confirmationmethodBL1', to='checksheet.ConfirmationMethod', verbose_name='确认方法BL1')),
                ('确认方法2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confirmationmethodBL2', to='checksheet.ConfirmationMethod', verbose_name='确认方法BL2')),
                ('确认方法3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confirmationmethodBL3', to='checksheet.ConfirmationMethod', verbose_name='确认方法BL3')),
                ('确认方法4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confirmationmethodBL4', to='checksheet.ConfirmationMethod', verbose_name='确认方法BL4')),
                ('确认方法5', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confirmationmethodBL5', to='checksheet.ConfirmationMethod', verbose_name='确认方法BL5')),
                ('确认方法6', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confirmationmethodBL6', to='checksheet.ConfirmationMethod', verbose_name='确认方法BL6')),
                ('确认方法7', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confirmationmethodBL7', to='checksheet.ConfirmationMethod', verbose_name='确认方法BL7')),
                ('确认频次1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confirmationfrequencyBL1', to='checksheet.ConfirmationFrequency', verbose_name='确认频次BL1')),
                ('确认频次2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confirmationfrequencyBL2', to='checksheet.ConfirmationFrequency', verbose_name='确认频次BL2')),
                ('确认频次3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confirmationfrequencyBL3', to='checksheet.ConfirmationFrequency', verbose_name='确认频次BL3')),
                ('确认频次4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confirmationfrequencyBL4', to='checksheet.ConfirmationFrequency', verbose_name='确认频次BL4')),
                ('确认频次5', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confirmationfrequencyBL5', to='checksheet.ConfirmationFrequency', verbose_name='确认频次BL5')),
                ('确认频次6', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confirmationfrequencyBL6', to='checksheet.ConfirmationFrequency', verbose_name='确认频次BL6')),
                ('确认频次7', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confirmationfrequencyBL7', to='checksheet.ConfirmationFrequency', verbose_name='确认频次BL7')),
                ('管理项目1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manageprojectBL1', to='checksheet.ManageProject', verbose_name='管理项目BL1')),
                ('管理项目2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manageprojectBL2', to='checksheet.ManageProject', verbose_name='管理项目BL2')),
                ('管理项目3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manageprojectBL3', to='checksheet.ManageProject', verbose_name='管理项目BL3')),
                ('管理项目4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manageprojectBL4', to='checksheet.ManageProject', verbose_name='管理项目BL4')),
                ('管理项目5', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manageprojectBL5', to='checksheet.ManageProject', verbose_name='管理项目BL5')),
                ('管理项目6', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manageprojectBL6', to='checksheet.ManageProject', verbose_name='管理项目BL6')),
                ('管理项目7', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manageprojectBL7', to='checksheet.ManageProject', verbose_name='管理项目BL7')),
            ],
            options={
                'ordering': ['parts_code'],
            },
        ),
    ]
