# Generated by Django 3.0 on 2021-06-09 08:17

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('checksheet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckSheet',
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
                ('拉延模压力设定', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('模块高度设定', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('气垫顶出高度设定', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True)),
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
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('last_updated_time', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('car_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='checksheet.CarType', verbose_name='car_type')),
                ('machine_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checksheet.MachineType')),
            ],
            options={
                'ordering': ['parts_code'],
            },
        ),
        migrations.CreateModel(
            name='ConfirmationFrequency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmation_frequency', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ConfirmationMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmation_method', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ManageProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manage_project', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='UpdateSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('部品番号', models.CharField(max_length=20, null=True)),
                ('部品名称', models.CharField(max_length=50, null=True)),
                ('机械名', models.CharField(max_length=10, null=True)),
                ('加工SPM', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('车型', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='checksheet.CarType', verbose_name='车型')),
            ],
            options={
                'ordering': ['-updated_time'],
            },
        ),
        migrations.DeleteModel(
            name='CheckSheets',
        ),
        migrations.AddField(
            model_name='checksheet',
            name='确认方法1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confirmationmethod1', to='checksheet.ConfirmationMethod', verbose_name='确认方法1'),
        ),
        migrations.AddField(
            model_name='checksheet',
            name='确认方法2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confirmationmethod2', to='checksheet.ConfirmationMethod', verbose_name='确认方法2'),
        ),
        migrations.AddField(
            model_name='checksheet',
            name='确认方法3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confirmationmethod3', to='checksheet.ConfirmationMethod', verbose_name='确认方法3'),
        ),
        migrations.AddField(
            model_name='checksheet',
            name='确认方法4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confirmationmethod4', to='checksheet.ConfirmationMethod', verbose_name='确认方法4'),
        ),
        migrations.AddField(
            model_name='checksheet',
            name='确认方法5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confirmationmethod5', to='checksheet.ConfirmationMethod', verbose_name='确认方法5'),
        ),
        migrations.AddField(
            model_name='checksheet',
            name='确认方法6',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confirmationmethod6', to='checksheet.ConfirmationMethod', verbose_name='确认方法6'),
        ),
        migrations.AddField(
            model_name='checksheet',
            name='确认方法7',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confirmationmethod7', to='checksheet.ConfirmationMethod', verbose_name='确认方法7'),
        ),
        migrations.AddField(
            model_name='checksheet',
            name='确认频次1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confirmationfrequency1', to='checksheet.ConfirmationFrequency', verbose_name='确认频次1'),
        ),
        migrations.AddField(
            model_name='checksheet',
            name='确认频次2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confirmationfrequency2', to='checksheet.ConfirmationFrequency', verbose_name='确认频次2'),
        ),
        migrations.AddField(
            model_name='checksheet',
            name='确认频次3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confirmationfrequency3', to='checksheet.ConfirmationFrequency', verbose_name='确认频次3'),
        ),
        migrations.AddField(
            model_name='checksheet',
            name='确认频次4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confirmationfrequency4', to='checksheet.ConfirmationFrequency', verbose_name='确认频次4'),
        ),
        migrations.AddField(
            model_name='checksheet',
            name='确认频次5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confirmationfrequency5', to='checksheet.ConfirmationFrequency', verbose_name='确认频次5'),
        ),
        migrations.AddField(
            model_name='checksheet',
            name='确认频次6',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confirmationfrequency6', to='checksheet.ConfirmationFrequency', verbose_name='确认频次6'),
        ),
        migrations.AddField(
            model_name='checksheet',
            name='确认频次7',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confirmationfrequency7', to='checksheet.ConfirmationFrequency', verbose_name='确认频次7'),
        ),
        migrations.AddField(
            model_name='checksheet',
            name='管理项目1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manageproject1', to='checksheet.ManageProject', verbose_name='管理项目1'),
        ),
        migrations.AddField(
            model_name='checksheet',
            name='管理项目2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manageproject2', to='checksheet.ManageProject', verbose_name='管理项目2'),
        ),
        migrations.AddField(
            model_name='checksheet',
            name='管理项目3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manageproject3', to='checksheet.ManageProject', verbose_name='管理项目3'),
        ),
        migrations.AddField(
            model_name='checksheet',
            name='管理项目4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manageproject4', to='checksheet.ManageProject', verbose_name='管理项目4'),
        ),
        migrations.AddField(
            model_name='checksheet',
            name='管理项目5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manageproject5', to='checksheet.ManageProject', verbose_name='管理项目5'),
        ),
        migrations.AddField(
            model_name='checksheet',
            name='管理项目6',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manageproject6', to='checksheet.ManageProject', verbose_name='管理项目6'),
        ),
        migrations.AddField(
            model_name='checksheet',
            name='管理项目7',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manageproject7', to='checksheet.ManageProject', verbose_name='管理项目7'),
        ),
    ]
