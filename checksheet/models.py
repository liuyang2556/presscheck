# import re
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from ckeditor_uploader.fields import RichTextUploadingField
# from django.core.validators import MaxValueValidator, MinValueValidator
# from ckeditor.fields import RichTextField
# from django.urls import reverse


class CarType(models.Model):
    type_name = models.CharField(max_length=10)
    def __str__(self):
        return self.type_name

class MachineType(models.Model):
    machine_name = models.CharField(max_length=10)
    def __str__(self):
        return self.machine_name

class ManageProject(models.Model):
    manage_project = models.CharField(max_length=10)
    def __str__(self):
        return self.manage_project

class ConfirmationMethod(models.Model):
    confirmation_method = models.CharField(max_length=10)
    # manage_project = models.ForeignKey(ManageProject, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.confirmation_method

class ConfirmationFrequency(models.Model):
    confirmation_frequency = models.CharField(max_length=10)
    # manage_project = models.ForeignKey(ManageProject, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.confirmation_frequency

class CheckSheet(models.Model):
    管理编号 = models.CharField(max_length=10, blank=True, null=True)
    parts_code = models.CharField(max_length=20, blank=True, null=True)
    parts_name = models.CharField(max_length=50, blank=True, null=True)
    car_type = models.ForeignKey(CarType, on_delete=models.CASCADE, verbose_name='car_type', blank = True, null=True)
    machine_type = models.ForeignKey(MachineType, on_delete=models.CASCADE)
    标准spm = models.DecimalField(max_digits = 3, decimal_places = 1, blank=True, null=True)
    容器 = models.CharField(max_length=5, blank=True, null=True)
    SNP = models.IntegerField(default=0, blank=True, null=True)
    材质 = models.CharField(max_length=20, blank=True, null=True)
    板厚 = models.CharField(max_length=20, blank=True, null=True)
    标准材料宽度 = models.IntegerField(default=0, blank=True, null=True)
    进给量 = models.DecimalField(max_digits = 5, decimal_places = 1, blank=True, null=True)
    拉延模压力设定 = models.DecimalField(max_digits = 3, decimal_places = 2, blank=True, null=True)
    模块高度设定 = models.DecimalField(max_digits = 5, decimal_places = 1, blank=True, null=True)
    气垫顶出高度设定 = models.DecimalField(max_digits = 4, decimal_places = 1, blank=True, null=True)
    发生日1 = models.DateField(blank=True, null=True)
    发生日2 = models.DateField(blank=True, null=True)
    发生日3 = models.DateField(blank=True, null=True)
    不合格内容1 = models.CharField(max_length=100, blank=True, null=True)
    不合格内容2 = models.CharField(max_length=100, blank=True, null=True)
    不合格内容3 = models.CharField(max_length=100, blank=True, null=True)
    发生原因1 = models.CharField(max_length=100, blank=True, null=True)
    发生原因2 = models.CharField(max_length=100, blank=True, null=True)
    发生原因3 = models.CharField(max_length=100, blank=True, null=True)
    管理项目1 = models.ForeignKey(ManageProject, related_name='manageproject1', verbose_name='管理项目1', on_delete=models.CASCADE, blank=True, null=True)
    规格值1 = models.CharField(max_length=20, blank=True, null=True)
    确认方法1 = models.ForeignKey(ConfirmationMethod, related_name='confirmationmethod1', verbose_name='确认方法1',on_delete=models.CASCADE, blank=True, null=True)
    确认频次1 = models.ForeignKey(ConfirmationFrequency, related_name='confirmationfrequency1', verbose_name='确认频次1',on_delete=models.CASCADE, blank=True, null=True)
    管理项目2 = models.ForeignKey(ManageProject, related_name='manageproject2', verbose_name='管理项目2', on_delete=models.CASCADE, blank=True, null=True)
    规格值2 = models.CharField(max_length=20, blank=True, null=True)
    确认方法2 = models.ForeignKey(ConfirmationMethod, related_name='confirmationmethod2', verbose_name='确认方法2',on_delete=models.CASCADE, blank=True, null=True)
    确认频次2 = models.ForeignKey(ConfirmationFrequency, related_name='confirmationfrequency2', verbose_name='确认频次2',on_delete=models.CASCADE, blank=True, null=True)
    管理项目3 = models.ForeignKey(ManageProject, related_name='manageproject3', verbose_name='管理项目3', on_delete=models.CASCADE, blank=True, null=True)
    规格值3 = models.CharField(max_length=20, blank=True, null=True)
    确认方法3 = models.ForeignKey(ConfirmationMethod, related_name='confirmationmethod3', verbose_name='确认方法3',on_delete=models.CASCADE, blank=True, null=True)
    确认频次3 = models.ForeignKey(ConfirmationFrequency, related_name='confirmationfrequency3', verbose_name='确认频次3',on_delete=models.CASCADE, blank=True, null=True)
    管理项目4 = models.ForeignKey(ManageProject, related_name='manageproject4', verbose_name='管理项目4', on_delete=models.CASCADE, blank=True, null=True)
    规格值4 = models.CharField(max_length=20, blank=True, null=True)
    确认方法4 = models.ForeignKey(ConfirmationMethod, related_name='confirmationmethod4', verbose_name='确认方法4',on_delete=models.CASCADE, blank=True, null=True)
    确认频次4 = models.ForeignKey(ConfirmationFrequency, related_name='confirmationfrequency4', verbose_name='确认频次4',on_delete=models.CASCADE, blank=True, null=True)
    管理项目5 = models.ForeignKey(ManageProject, related_name='manageproject5', verbose_name='管理项目5', on_delete=models.CASCADE, blank=True, null=True)
    规格值5 = models.CharField(max_length=20, blank=True, null=True)
    确认方法5 = models.ForeignKey(ConfirmationMethod, related_name='confirmationmethod5', verbose_name='确认方法5',on_delete=models.CASCADE, blank=True, null=True)
    确认频次5 = models.ForeignKey(ConfirmationFrequency, related_name='confirmationfrequency5', verbose_name='确认频次5',on_delete=models.CASCADE, blank=True, null=True)
    管理项目6 = models.ForeignKey(ManageProject, related_name='manageproject6', verbose_name='管理项目6', on_delete=models.CASCADE, blank=True, null=True)
    规格值6 = models.CharField(max_length=20, blank=True, null=True)
    确认方法6 = models.ForeignKey(ConfirmationMethod, related_name='confirmationmethod6', verbose_name='确认方法6',on_delete=models.CASCADE, blank=True, null=True)
    确认频次6 = models.ForeignKey(ConfirmationFrequency, related_name='confirmationfrequency6', verbose_name='确认频次6',on_delete=models.CASCADE, blank=True, null=True)
    管理项目7 = models.ForeignKey(ManageProject, related_name='manageproject7', verbose_name='管理项目7', on_delete=models.CASCADE, blank=True, null=True)
    规格值7 = models.CharField(max_length=20, blank=True, null=True)
    确认方法7 = models.ForeignKey(ConfirmationMethod, related_name='confirmationmethod7', verbose_name='确认方法7',on_delete=models.CASCADE, blank=True, null=True)
    确认频次7 = models.ForeignKey(ConfirmationFrequency, related_name='confirmationfrequency7', verbose_name='确认频次7',on_delete=models.CASCADE, blank=True, null=True)
    # checkpartern = models.ForeignKey(CheckPartern, on_delete=models.CASCADE, blank=True, null=True)


    content1 = RichTextUploadingField()
    content2 = RichTextUploadingField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # read_details = GenericRelation(ReadDetail)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "<CheckSheet: %s>" % self.car_type
    class Meta:
        # ordering = ['-created_time']
        ordering = ['parts_code']

class UpdateSheet(models.Model):
    contenttype = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('contenttype', 'object_id')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_time = models.DateTimeField(auto_now=True)

    # 以下为直接调用数据库的内容
    manage_num = models.CharField(max_length=10, blank=True, null=True)
    部品番号 = models.CharField(max_length=20, null=True)
    部品名称 = models.CharField(max_length=50, null=True)
    # 车型 = models.ForeignKey(CarType, on_delete=models.CASCADE, verbose_name='车型', blank = True, null=True)
    车型 = models.CharField(max_length=20, null=True)
    机械名 = models.CharField(max_length=10, null=True)
    standard_spm =  models.CharField(max_length=10, null=True)
    container = models.CharField(max_length=5, blank=True, null=True)
    SNPs = models.IntegerField(default=0, blank=True, null=True)
    material = models.CharField(max_length=20, blank=True, null=True)
    thickness = models.CharField(max_length=20, blank=True, null=True)
    # 加工日 = models.CharField(max_length=20, blank=True, null=True)
    标准材料宽度 = models.IntegerField(default=0, blank=True, null=True)
    进给量 = models.DecimalField(max_digits = 5, decimal_places = 1, blank=True, null=True)

    draw_set = models.CharField(max_length=10, blank=True, null=True)
    diehight_set = models.CharField(max_length=10, blank=True, null=True)
    cushion_set = models.CharField(max_length=10, blank=True, null=True)

    manage_pj1 = models.CharField(max_length=10, blank=True, null=True)
    confirmation_meth1 = models.CharField(max_length=10, blank=True, null=True)
    confirmation_fre1 = models.CharField(max_length=10, blank=True, null=True)
    manage_pj2 = models.CharField(max_length=10, blank=True, null=True)
    confirmation_meth2 = models.CharField(max_length=10, blank=True, null=True)
    confirmation_fre2 = models.CharField(max_length=10, blank=True, null=True)
    manage_pj3 = models.CharField(max_length=10, blank=True, null=True)
    confirmation_meth3 = models.CharField(max_length=10, blank=True, null=True)
    confirmation_fre3 = models.CharField(max_length=10, blank=True, null=True)
    manage_pj4 = models.CharField(max_length=10, blank=True, null=True)
    confirmation_meth4 = models.CharField(max_length=10, blank=True, null=True)
    confirmation_fre4 = models.CharField(max_length=10, blank=True, null=True)
    manage_pj5 = models.CharField(max_length=10, blank=True, null=True)
    confirmation_meth5 = models.CharField(max_length=10, blank=True, null=True)
    confirmation_fre5 = models.CharField(max_length=10, blank=True, null=True)
    manage_pj6 = models.CharField(max_length=10, blank=True, null=True)
    confirmation_meth6 = models.CharField(max_length=10, blank=True, null=True)
    confirmation_fre6 = models.CharField(max_length=10, blank=True, null=True)
    manage_pj7 = models.CharField(max_length=10, blank=True, null=True)
    confirmation_meth7 = models.CharField(max_length=10, blank=True, null=True)
    confirmation_fre7 = models.CharField(max_length=10, blank=True, null=True)
    manage_spec1 = models.CharField(max_length=20, blank=True, null=True)
    manage_spec2 = models.CharField(max_length=20, blank=True, null=True)
    manage_spec3 = models.CharField(max_length=20, blank=True, null=True)
    manage_spec4 = models.CharField(max_length=20, blank=True, null=True)
    manage_spec5 = models.CharField(max_length=20, blank=True, null=True)
    manage_spec6 = models.CharField(max_length=20, blank=True, null=True)
    manage_spec7 = models.CharField(max_length=20, blank=True, null=True)



    # 以下为前端页面Input的内容
    加工SPM = models.CharField(max_length=10, null=True)
    卷材代号 = models.CharField(max_length=20, blank=True, null=True)
    拉延模压力 = models.CharField(max_length=10, blank=True, null=True)
    模具高度 = models.CharField(max_length=10, blank=True, null=True)
    气垫顶出高度 = models.CharField(max_length=10, blank=True, null=True)
    生产数 = models.IntegerField(default=0, blank=True, null=True)
    合格数 = models.IntegerField(default=0, blank=True, null=True)
    不良数 = models.IntegerField(default=0, blank=True, null=True)
    模具修理 = models.CharField(max_length=10, blank=True, null=True)

    模具检查清扫 = models.CharField(max_length=10, blank=True, null=True)
    加工批次号 = models.CharField(max_length=20, blank=True, null=True)
    计划数量 = models.CharField(max_length=10, blank=True, null=True)

    机械修理 = models.CharField(max_length=10, blank=True, null=True)
    人手替换 = models.CharField(max_length=10, blank=True, null=True)
    使用冲床 = models.CharField(max_length=10, blank=True, null=True)
    设变号 = models.CharField(max_length=10, blank=True, null=True)
    BL材生产日期1 = models.CharField(max_length=20, blank=True, null=True)
    BL材生产日期2 = models.CharField(max_length=20, blank=True, null=True)
    BL材批次号1 = models.CharField(max_length=30, blank=True, null=True)
    BL材批次号2 = models.CharField(max_length=30, blank=True, null=True)

    初检时间 = models.CharField(max_length=10, blank=True, null=True)
    管理项目11 = models.CharField(max_length=10, blank=True, null=True)
    管理项目12 = models.CharField(max_length=10, blank=True, null=True)
    管理项目13 = models.CharField(max_length=10, blank=True, null=True)
    管理项目14 = models.CharField(max_length=10, blank=True, null=True)
    规格值15 = models.CharField(max_length=20, blank=True, null=True)
    规格值16 = models.CharField(max_length=20, blank=True, null=True)
    规格值17 = models.CharField(max_length=20, blank=True, null=True)
    二次确认1 = models.CharField(max_length=10, blank=True, null=True)

    中检时间 = models.CharField(max_length=10, blank=True, null=True)
    中检生产数 = models.CharField(max_length=10, blank=True, null=True)
    管理项目21 = models.CharField(max_length=10, blank=True, null=True)
    管理项目22 = models.CharField(max_length=10, blank=True, null=True)
    管理项目23 = models.CharField(max_length=10, blank=True, null=True)
    管理项目24 = models.CharField(max_length=10, blank=True, null=True)
    规格值25 = models.CharField(max_length=20, blank=True, null=True)
    规格值26 = models.CharField(max_length=20, blank=True, null=True)
    规格值27 = models.CharField(max_length=20, blank=True, null=True)
    二次确认2 = models.CharField(max_length=10, blank=True, null=True)

    终检时间 = models.CharField(max_length=10, blank=True, null=True)
    终检生产数 = models.CharField(max_length=10, blank=True, null=True)
    管理项目31 = models.CharField(max_length=10, blank=True, null=True)
    管理项目32 = models.CharField(max_length=10, blank=True, null=True)
    管理项目33 = models.CharField(max_length=10, blank=True, null=True)
    管理项目34 = models.CharField(max_length=10, blank=True, null=True)
    规格值35 = models.CharField(max_length=20, blank=True, null=True)
    规格值36 = models.CharField(max_length=20, blank=True, null=True)
    规格值37 = models.CharField(max_length=20, blank=True, null=True)
    二次确认3 = models.CharField(max_length=10, blank=True, null=True)

    occur_day1 = models.CharField(max_length=10, blank=True, null=True)
    unqualified1 = models.CharField(max_length=100, blank=True, null=True)
    occur_reason1 = models.CharField(max_length=100, blank=True, null=True)
    occur_day2 = models.CharField(max_length=10, blank=True, null=True)
    unqualified2 = models.CharField(max_length=100, blank=True, null=True)
    occur_reason2 = models.CharField(max_length=100, blank=True, null=True)
    occur_day3 = models.CharField(max_length=10, blank=True, null=True)
    unqualified3 = models.CharField(max_length=100, blank=True, null=True)
    occur_reason3 = models.CharField(max_length=100, blank=True, null=True)
    初1 = models.CharField(max_length=10, blank=True, null=True)
    中1 = models.CharField(max_length=10, blank=True, null=True)
    终1 = models.CharField(max_length=10, blank=True, null=True)
    初2 = models.CharField(max_length=10, blank=True, null=True)
    中2 = models.CharField(max_length=10, blank=True, null=True)
    终2 = models.CharField(max_length=10, blank=True, null=True)
    初3 = models.CharField(max_length=10, blank=True, null=True)
    中3 = models.CharField(max_length=10, blank=True, null=True)
    终3 = models.CharField(max_length=10, blank=True, null=True)

    检具1 = models.CharField(max_length=10, blank=True, null=True)
    检具2 = models.CharField(max_length=10, blank=True, null=True)
    检具3 = models.CharField(max_length=10, blank=True, null=True)
    检具4 = models.CharField(max_length=10, blank=True, null=True)
    检具5 = models.CharField(max_length=10, blank=True, null=True)
    检具6 = models.CharField(max_length=10, blank=True, null=True)
    检具7 = models.CharField(max_length=10, blank=True, null=True)
    检具8 = models.CharField(max_length=10, blank=True, null=True)

    初检1 = models.CharField(max_length=10, blank=True, null=True)
    初检2 = models.CharField(max_length=10, blank=True, null=True)
    初检3 = models.CharField(max_length=10, blank=True, null=True)
    初检4 = models.CharField(max_length=10, blank=True, null=True)
    初检5 = models.CharField(max_length=10, blank=True, null=True)
    中检1 = models.CharField(max_length=10, blank=True, null=True)
    中检2 = models.CharField(max_length=10, blank=True, null=True)
    中检3 = models.CharField(max_length=10, blank=True, null=True)
    中检4 = models.CharField(max_length=10, blank=True, null=True)
    中检5 = models.CharField(max_length=10, blank=True, null=True)
    终检1 = models.CharField(max_length=10, blank=True, null=True)
    终检2 = models.CharField(max_length=10, blank=True, null=True)
    终检3 = models.CharField(max_length=10, blank=True, null=True)
    终检4 = models.CharField(max_length=10, blank=True, null=True)
    终检5 = models.CharField(max_length=10, blank=True, null=True)

    初检21 = models.CharField(max_length=10, blank=True, null=True)
    初检22 = models.CharField(max_length=10, blank=True, null=True)
    初检23 = models.CharField(max_length=10, blank=True, null=True)
    初检24 = models.CharField(max_length=10, blank=True, null=True)
    初检25 = models.CharField(max_length=10, blank=True, null=True)
    中检21 = models.CharField(max_length=10, blank=True, null=True)
    中检22 = models.CharField(max_length=10, blank=True, null=True)
    中检23 = models.CharField(max_length=10, blank=True, null=True)
    中检24 = models.CharField(max_length=10, blank=True, null=True)
    中检25 = models.CharField(max_length=10, blank=True, null=True)
    终检21 = models.CharField(max_length=10, blank=True, null=True)
    终检22 = models.CharField(max_length=10, blank=True, null=True)
    终检23 = models.CharField(max_length=10, blank=True, null=True)
    终检24 = models.CharField(max_length=10, blank=True, null=True)
    终检25 = models.CharField(max_length=10, blank=True, null=True)

    确认点位1 = models.CharField(max_length=500, blank=True, null=True)
    确认点位2 = models.CharField(max_length=500, blank=True, null=True)

    作业员A = models.CharField(max_length=10, blank=True, null=True)
    作业员B = models.CharField(max_length=10, blank=True, null=True)
    作业员C = models.CharField(max_length=10, blank=True, null=True)
    作业员D = models.CharField(max_length=10, blank=True, null=True)

    备注 = models.CharField(max_length=150, blank=True, null=True)

    卷材号1 = models.CharField(max_length=20, blank=True, null=True)
    板厚1_1 = models.CharField(max_length=10, blank=True, null=True)
    板厚2_1 = models.CharField(max_length=10, blank=True, null=True)
    宽度1 = models.CharField(max_length=10, blank=True, null=True)
    生产数量1 = models.CharField(max_length=10, blank=True, null=True)
    完成1_1 = models.CharField(max_length=10, blank=True, null=True)
    完成2_1 = models.CharField(max_length=10, blank=True, null=True)

    卷材号2 = models.CharField(max_length=20, blank=True, null=True)
    板厚1_2 = models.CharField(max_length=10, blank=True, null=True)
    板厚2_2 = models.CharField(max_length=10, blank=True, null=True)
    宽度2 = models.CharField(max_length=10, blank=True, null=True)
    生产数量2 = models.CharField(max_length=10, blank=True, null=True)
    完成1_2 = models.CharField(max_length=10, blank=True, null=True)
    完成2_2 = models.CharField(max_length=10, blank=True, null=True)

    卷材号3 = models.CharField(max_length=20, blank=True, null=True)
    板厚1_3 = models.CharField(max_length=10, blank=True, null=True)
    板厚2_3 = models.CharField(max_length=10, blank=True, null=True)
    宽度3 = models.CharField(max_length=10, blank=True, null=True)
    生产数量3 = models.CharField(max_length=10, blank=True, null=True)
    完成1_3 = models.CharField(max_length=10, blank=True, null=True)
    完成2_3 = models.CharField(max_length=10, blank=True, null=True)

    卷材号4 = models.CharField(max_length=20, blank=True, null=True)
    板厚1_4 = models.CharField(max_length=10, blank=True, null=True)
    板厚2_4 = models.CharField(max_length=10, blank=True, null=True)
    宽度4 = models.CharField(max_length=10, blank=True, null=True)
    生产数量4 = models.CharField(max_length=10, blank=True, null=True)
    完成1_4 = models.CharField(max_length=10, blank=True, null=True)
    完成2_4 = models.CharField(max_length=10, blank=True, null=True)

    卷材号5 = models.CharField(max_length=20, blank=True, null=True)
    板厚1_5 = models.CharField(max_length=10, blank=True, null=True)
    板厚2_5 = models.CharField(max_length=10, blank=True, null=True)
    宽度5 = models.CharField(max_length=10, blank=True, null=True)
    生产数量5 = models.CharField(max_length=10, blank=True, null=True)
    完成1_5 = models.CharField(max_length=10, blank=True, null=True)
    完成2_5 = models.CharField(max_length=10, blank=True, null=True)

    卷材号6 = models.CharField(max_length=20, blank=True, null=True)
    板厚1_6 = models.CharField(max_length=10, blank=True, null=True)
    板厚2_6 = models.CharField(max_length=10, blank=True, null=True)
    宽度6 = models.CharField(max_length=10, blank=True, null=True)
    生产数量6 = models.CharField(max_length=10, blank=True, null=True)
    完成1_6 = models.CharField(max_length=10, blank=True, null=True)
    完成2_6 = models.CharField(max_length=10, blank=True, null=True)

    卷材号7 = models.CharField(max_length=20, blank=True, null=True)
    板厚1_7 = models.CharField(max_length=10, blank=True, null=True)
    板厚2_7 = models.CharField(max_length=10, blank=True, null=True)
    宽度7 = models.CharField(max_length=10, blank=True, null=True)
    生产数量7 = models.CharField(max_length=10, blank=True, null=True)
    完成1_7 = models.CharField(max_length=10, blank=True, null=True)
    完成2_7 = models.CharField(max_length=10, blank=True, null=True)



     # 以上内容以确认OK

    def __str__(self):
        return "<UpdateSheet: %s>" % self.部品番号
    class Meta:
        # ordering = ['-created_time']
        ordering = ['-updated_time']

