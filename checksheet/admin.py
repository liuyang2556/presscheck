from django.contrib import admin
from .models import CarType, MachineType, CheckSheet, ManageProject, ConfirmationMethod, ConfirmationFrequency, UpdateSheet

# @admin.register(ManageProject)

@admin.register(CarType)
class CarTypeAdmin(admin.ModelAdmin):
    list_display = ('id','type_name')
    list_display_links = ("id",'type_name')

@admin.register(MachineType)
class MachineTypeAdmin(admin.ModelAdmin):
    list_display = ('id','machine_name')
    # list_display_links = ("id",'machine_name')
    list_editable = ['machine_name']

@admin.register(ManageProject)
class ManageProjectAdmin(admin.ModelAdmin):
    list_display = ('id','manage_project')

@admin.register(ConfirmationMethod)
class ConfirmationMethodAdmin(admin.ModelAdmin):
    list_display = ('id','confirmation_method')

@admin.register(ConfirmationFrequency)
class ConfirmationFrequencyAdmin(admin.ModelAdmin):
    list_display = ('id','confirmation_frequency')

# @admin.register(CheckPartern)
# class CheckParternAdmin(admin.ModelAdmin):
#     list_display = ('id','check_partern')

@admin.register(CheckSheet)
class CheckSheetAdmin(admin.ModelAdmin):

    list_display = ('id', 'parts_code', 'parts_name', 'car_type', 'machine_type', 'author', 'created_time', 'last_updated_time')
    list_display_links = ("id",'parts_code', 'parts_name')
    fieldsets = (
        ("基础信息", {'fields': (('管理编号', 'parts_code'), ('parts_name', 'car_type', 'machine_type'))}),
        ("基础设定", {'fields':(('标准spm', '容器', 'SNP'), ('材质', '板厚'), ('标准材料宽度', '进给量'), ('拉延模压力设定', '模块高度设定', '气垫顶出高度设定'))}),
        ("过往不良设定", {'fields':('发生日1', ('不合格内容1', '发生原因1'), '发生日2', ('不合格内容2', '发生原因2'), '发生日3', ('不合格内容3', '发生原因3'))}),
        ("管理项目", {'fields':(
            '管理项目1', ('规格值1','确认方法1', '确认频次1'),
            '管理项目2', ('规格值2','确认方法2', '确认频次2'),
            '管理项目3', ('规格值3','确认方法3', '确认频次3'),
            '管理项目4', ('规格值4','确认方法4', '确认频次4'),
            '管理项目5', ('规格值5','确认方法5', '确认频次5'),
            '管理项目6', ('规格值6','确认方法6', '确认频次6'),
            '管理项目7', ('规格值7','确认方法7', '确认频次7'),
            'content1',
            'content2',
            )}),

    )

# @admin.register(CheckSheetBL)
# class CheckSheetBLAdmin(admin.ModelAdmin):

#     list_display = ('id', 'parts_code', 'parts_name', 'car_type', 'machine_type', 'author', 'created_time', 'last_updated_time')
#     list_display_links = ("id",'parts_code', 'parts_name')
#     fieldsets = (
#         ("基础信息", {'fields': (('管理编号', 'parts_code'), ('parts_name', 'car_type', 'machine_type'))}),
#         ("基础设定", {'fields':(('标准spm', '加工模高设定', 'SNP'), ('材质', '板厚'), ('标准材料宽度', '进给量'))}),
#         ("过往不良设定", {'fields':('发生日1', ('不合格内容1', '发生原因1'), '发生日2', ('不合格内容2', '发生原因2'), '发生日3', ('不合格内容3', '发生原因3'))}),
#         ("管理项目", {'fields':(
#             '管理项目1', ('规格值1','确认方法1', '确认频次1'),
#             '管理项目2', ('规格值2','确认方法2', '确认频次2'),
#             '管理项目3', ('规格值3','确认方法3', '确认频次3'),
#             '管理项目4', ('规格值4','确认方法4', '确认频次4'),
#             '管理项目5', ('规格值5','确认方法5', '确认频次5'),
#             '管理项目6', ('规格值6','确认方法6', '确认频次6'),
#             '管理项目7', ('规格值7','确认方法7', '确认频次7'),
#             'content1',
#             'content2',
#             )}),

#     )

@admin.register(UpdateSheet)
class UpdateSheetAdmin(admin.ModelAdmin):
    list_display = ('id', '部品番号', '部品名称', '加工SPM', 'updated_time', 'user')
    list_display_links = ('id', '部品番号', '部品名称')
