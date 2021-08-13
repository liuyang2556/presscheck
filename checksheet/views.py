from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db.models import Count
from django.urls import reverse
# from django.db.models import DoesNotExist

from .models import CheckSheet, CarType, MachineType, ManageProject, ConfirmationMethod, ConfirmationFrequency, UpdateSheet

def get_checksheet_list_common_data(request, cheeksheets_all_list):
    paginator = Paginator(cheeksheets_all_list, settings.EACH_PAGE_CHEEKSHEETS_NUMBER)
    page_num = request.GET.get('page', 1)  #获取url的页面参数（GET请求）
    page_of_checksheets = paginator.get_page(page_num)
    current_page_num = page_of_checksheets.number  # 获取当前页码
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                 list(range(current_page_num, min(current_page_num + 2, paginator.num_pages + 1)))
    # 加上省略页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    #加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context = {}
    context['checksheets'] = page_of_checksheets.object_list
    context['page_of_checksheets'] = page_of_checksheets
    context['page_range'] = page_range
    context['car_types'] = CarType.objects.annotate(checksheet_count=Count('checksheet'))
    return context

def checksheet_list(request):
    cheeksheets_all_list = CheckSheet.objects.all()

    context = get_checksheet_list_common_data(request, cheeksheets_all_list)
    return render(request,'checksheet/checksheet_list.html',context)

def cars_with_type(request, car_type_pk):
    car_type = get_object_or_404(CarType, pk=car_type_pk)
    cheeksheets_all_list = CheckSheet.objects.filter(car_type=car_type)
    context = get_checksheet_list_common_data(request, cheeksheets_all_list)
    context['car_type'] = car_type
    return render(request,'checksheet/cars_with_type.html',context)

def checksheet_page(request, checksheet_pk):
    checksheet = get_object_or_404(CheckSheet, pk=checksheet_pk)
    manage_num_one = CheckSheet.objects.filter(parts_code=checksheet.parts_code).values_list("管理编号", flat=True)[0][0]
    prg_or_bl = CheckSheet.objects.filter(parts_code=checksheet.parts_code).values_list("parts_code", flat=True)[0][::-1][0:2]

    context = {}
    context['checksheet'] = checksheet
    context['manage_num_one'] = manage_num_one
    context['prg_or_bl'] = prg_or_bl

    response = render(request,'checksheet/checksheet_page.html',context)
    return response

def get_updatesheet_list_common_data(request, updatesheets_all_list):
    paginator = Paginator(updatesheets_all_list, settings.EACH_PAGE_CHEEKSHEETS_NUMBER)
    page_num = request.GET.get('page', 1)  #获取url的页面参数（GET请求）
    page_of_updatesheets = paginator.get_page(page_num)
    current_page_num = page_of_updatesheets.number  # 获取当前页码
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                 list(range(current_page_num, min(current_page_num + 2, paginator.num_pages + 1)))
    # 加上省略页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    #加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context = {}
    context['updatesheets'] = page_of_updatesheets.object_list
    context['page_of_updatesheets'] = page_of_updatesheets
    context['page_range'] = page_range
    # context['车型s'] = CarType.objects.annotate(updatesheet_count=Count('updatesheet'))
    return context

def updatesheet_list(request):
    updatesheets_all_list = UpdateSheet.objects.all()
    context = get_updatesheet_list_common_data(request, updatesheets_all_list)
    return render(request,'updatesheet/updatesheet_list.html',context)

def updatesheet_data(request):
    user = request.user
    contenttype = request.POST.get('contenttype','')
    object_id = int(request.POST.get('object_id',''))
    model_class = ContentType.objects.get(model=contenttype).model_class()
    model_obj = model_class.objects.get(pk=object_id)
    # 以下为直接调用数据库的内容
    部品番号 = request.POST.get('部品番号', '')
    部品名称 = request.POST.get('部品名称', '')
    车型 = request.POST.get('车型', '')
    机械名 = request.POST.get('机械名', '')
    standard_spm = request.POST.get('standard_spm', '')
    manage_num = request.POST.get('manage_num', '')
    material = request.POST.get('material', '')
    thickness = request.POST.get('thickness', '')
    container = request.POST.get('container', '')
    SNPs = request.POST.get('SNPs', '')

    标准材料宽度 = request.POST.get('标准材料宽度', '')
    进给量 = request.POST.get('进给量', '')

    draw_set = request.POST.get('draw_set', '')
    diehight_set= request.POST.get('diehight_set', '')
    cushion_set = request.POST.get('cushion_set', '')
    manage_pj1 = request.POST.get('manage_pj1', '')
    manage_pj2 = request.POST.get('manage_pj2', '')
    manage_pj3 = request.POST.get('manage_pj3', '')
    manage_pj4 = request.POST.get('manage_pj4', '')
    manage_pj5 = request.POST.get('manage_pj5', '')
    manage_pj6 = request.POST.get('manage_pj6', '')
    manage_pj7 = request.POST.get('manage_pj7', '')
    confirmation_meth1 = request.POST.get('confirmation_meth1', '')
    confirmation_meth2 = request.POST.get('confirmation_meth2', '')
    confirmation_meth3 = request.POST.get('confirmation_meth3', '')
    confirmation_meth4 = request.POST.get('confirmation_meth4', '')
    confirmation_meth5 = request.POST.get('confirmation_meth5', '')
    confirmation_meth6 = request.POST.get('confirmation_meth6', '')
    confirmation_meth7 = request.POST.get('confirmation_meth7', '')
    confirmation_fre1 = request.POST.get('confirmation_fre1', '')
    confirmation_fre2 = request.POST.get('confirmation_fre2', '')
    confirmation_fre3 = request.POST.get('confirmation_fre3', '')
    confirmation_fre4 = request.POST.get('confirmation_fre4', '')
    confirmation_fre5 = request.POST.get('confirmation_fre5', '')
    confirmation_fre6 = request.POST.get('confirmation_fre6', '')
    confirmation_fre7 = request.POST.get('confirmation_fre7', '')
    manage_spec1 = request.POST.get('manage_spec1', '')
    manage_spec2 = request.POST.get('manage_spec2', '')
    manage_spec3 = request.POST.get('manage_spec3', '')
    manage_spec4 = request.POST.get('manage_spec4', '')
    manage_spec5 = request.POST.get('manage_spec5', '')
    manage_spec6 = request.POST.get('manage_spec6', '')
    manage_spec7 = request.POST.get('manage_spec7', '')
    occur_day1 = request.POST.get('occur_day1', '')
    unqualified1 = request.POST.get('unqualified1', '')
    occur_reason1 = request.POST.get('occur_reason1', '')
    occur_day2 = request.POST.get('occur_day2', '')
    unqualified2 = request.POST.get('unqualified2', '')
    occur_reason2 = request.POST.get('occur_reason2', '')
    occur_day3 = request.POST.get('occur_day3', '')
    unqualified3 = request.POST.get('unqualified3', '')
    occur_reason3 = request.POST.get('occur_reason3', '')
    # 以下为前端页面Input的内容
    加工SPM = request.POST.get('加工SPM', '')
    卷材代号 = request.POST.get('卷材代号', '')
    拉延模压力 = request.POST.get('拉延模压力', '')
    模具高度 = request.POST.get('模具高度', '')
    气垫顶出高度 = request.POST.get('气垫顶出高度', '')
    计划数量 = request.POST.get('计划数量', '')
    生产数 = request.POST.get('生产数', '')
    合格数 = request.POST.get('合格数', '')
    不良数 = request.POST.get('不良数', '')
    模具修理 = request.POST.get('模具修理', '')
    机械修理 = request.POST.get('机械修理', '')

    加工批次号 = request.POST.get('加工批次号', '')
    模具检查清扫 = request.POST.get('模具检查清扫', '')

    人手替换 = request.POST.get('人手替换', '')
    使用冲床 = request.POST.get('使用冲床', '')
    设变号 = request.POST.get('设变号', '')
    BL材生产日期1 = request.POST.get('BL材生产日期1', '')
    BL材生产日期2 = request.POST.get('BL材生产日期2', '')
    BL材批次号1 = request.POST.get('BL材批次号1', '')
    BL材批次号2 = request.POST.get('BL材批次号2', '')
    初检时间 = request.POST.get('初检时间', '')
    管理项目11 = request.POST.get('管理项目11', '')
    管理项目12 = request.POST.get('管理项目12', '')
    管理项目13 = request.POST.get('管理项目13', '')
    管理项目14 = request.POST.get('管理项目14', '')
    规格值15 = request.POST.get('规格值15', '')
    规格值16 = request.POST.get('规格值16', '')
    规格值17 = request.POST.get('规格值17', '')
    二次确认1 = request.POST.get('二次确认1', '')
    中检时间 = request.POST.get('中检时间', '')
    中检生产数 = request.POST.get('中检生产数', '')
    管理项目21 = request.POST.get('管理项目21', '')
    管理项目22 = request.POST.get('管理项目22', '')
    管理项目23 = request.POST.get('管理项目23', '')
    管理项目24 = request.POST.get('管理项目24', '')
    规格值25 = request.POST.get('规格值25', '')
    规格值26 = request.POST.get('规格值26', '')
    规格值27 = request.POST.get('规格值27', '')
    二次确认2 = request.POST.get('二次确认2', '')
    终检时间 = request.POST.get('终检时间', '')
    终检生产数 = request.POST.get('终检生产数', '')
    管理项目31 = request.POST.get('管理项目31', '')
    管理项目32 = request.POST.get('管理项目32', '')
    管理项目33 = request.POST.get('管理项目33', '')
    管理项目34 = request.POST.get('管理项目34', '')
    规格值35 = request.POST.get('规格值35', '')
    规格值36 = request.POST.get('规格值36', '')
    规格值37 = request.POST.get('规格值37', '')
    二次确认3 = request.POST.get('二次确认3', '')
    初1 = request.POST.get('初1', '')
    中1 = request.POST.get('中1', '')
    终1 = request.POST.get('终1', '')
    初2 = request.POST.get('初2', '')
    中2 = request.POST.get('中2', '')
    终2 = request.POST.get('终2', '')
    初3 = request.POST.get('初3', '')
    中3 = request.POST.get('中3', '')
    终3 = request.POST.get('终3', '')
    检具1 = request.POST.get('检具1', '')
    检具2 = request.POST.get('检具2', '')
    检具3 = request.POST.get('检具3', '')
    检具4 = request.POST.get('检具4', '')
    检具5 = request.POST.get('检具5', '')
    检具6 = request.POST.get('检具6', '')
    检具7 = request.POST.get('检具7', '')
    检具8 = request.POST.get('检具8', '')
    初检1 = request.POST.get('初检1', '')
    初检2 = request.POST.get('初检2', '')
    初检3 = request.POST.get('初检3', '')
    初检4 = request.POST.get('初检4', '')
    初检5 = request.POST.get('初检5', '')
    中检1 = request.POST.get('中检1', '')
    中检2 = request.POST.get('中检2', '')
    中检3 = request.POST.get('中检3', '')
    中检4 = request.POST.get('中检4', '')
    中检5 = request.POST.get('中检5', '')
    终检1 = request.POST.get('终检1', '')
    终检2 = request.POST.get('终检2', '')
    终检3 = request.POST.get('终检3', '')
    终检4 = request.POST.get('终检4', '')
    终检5 = request.POST.get('终检5', '')

    初检21 = request.POST.get('初检21', '')
    初检22 = request.POST.get('初检22', '')
    初检23 = request.POST.get('初检23', '')
    初检24 = request.POST.get('初检24', '')
    初检25 = request.POST.get('初检25', '')
    中检21 = request.POST.get('中检21', '')
    中检22 = request.POST.get('中检22', '')
    中检23 = request.POST.get('中检23', '')
    中检24 = request.POST.get('中检24', '')
    中检25 = request.POST.get('中检25', '')
    终检21 = request.POST.get('终检21', '')
    终检22 = request.POST.get('终检22', '')
    终检23 = request.POST.get('终检23', '')
    终检24 = request.POST.get('终检24', '')
    终检25 = request.POST.get('终检25', '')

    确认点位1 = request.POST.get('确认点位1', '')
    确认点位2 = request.POST.get('确认点位2', '')
    作业员A = request.POST.get('作业员A', '')
    作业员B = request.POST.get('作业员B', '')
    作业员C = request.POST.get('作业员C', '')
    作业员D = request.POST.get('作业员D', '')
    备注 = request.POST.get('备注', '')

    卷材号1 = request.POST.get('卷材号1', '')
    板厚1_1 = request.POST.get('板厚1-1', '')
    板厚2_1 = request.POST.get('板厚2-1', '')
    宽度1 = request.POST.get('宽度1', '')
    生产数量1 = request.POST.get('生产数量1', '')
    完成1_1 = request.POST.get('完成1-1', '')
    完成2_1 = request.POST.get('完成2-1', '')

    卷材号2 = request.POST.get('卷材号2', '')
    板厚1_2 = request.POST.get('板厚1-2', '')
    板厚2_2 = request.POST.get('板厚2-2', '')
    宽度2 = request.POST.get('宽度2', '')
    生产数量2 = request.POST.get('生产数量2', '')
    完成1_2 = request.POST.get('完成1-2', '')
    完成2_2 = request.POST.get('完成2-2', '')

    卷材号3 = request.POST.get('卷材号3', '')
    板厚1_3 = request.POST.get('板厚1-3', '')
    板厚2_3 = request.POST.get('板厚2-3', '')
    宽度3 = request.POST.get('宽度3', '')
    生产数量3 = request.POST.get('生产数量3', '')
    完成1_3 = request.POST.get('完成1-3', '')
    完成2_3 = request.POST.get('完成2-3', '')

    卷材号4 = request.POST.get('卷材号4', '')
    板厚1_4 = request.POST.get('板厚1-4', '')
    板厚2_4 = request.POST.get('板厚2-4', '')
    宽度4 = request.POST.get('宽度4', '')
    生产数量4 = request.POST.get('生产数量4', '')
    完成1_4 = request.POST.get('完成1-4', '')
    完成2_4 = request.POST.get('完成2-4', '')

    卷材号5 = request.POST.get('卷材号5', '')
    板厚1_5 = request.POST.get('板厚1-5', '')
    板厚2_5 = request.POST.get('板厚2-5', '')
    宽度5 = request.POST.get('宽度5', '')
    生产数量5 = request.POST.get('生产数量5', '')
    完成1_5 = request.POST.get('完成1-5', '')
    完成2_5 = request.POST.get('完成2-5', '')

    卷材号6 = request.POST.get('卷材号6', '')
    板厚1_6 = request.POST.get('板厚1-6', '')
    板厚2_6 = request.POST.get('板厚2-6', '')
    宽度6 = request.POST.get('宽度6', '')
    生产数量6 = request.POST.get('生产数量6', '')
    完成1_6 = request.POST.get('完成1-6', '')
    完成2_6 = request.POST.get('完成2-6', '')

    卷材号7 = request.POST.get('卷材号7', '')
    板厚1_7 = request.POST.get('板厚1-7', '')
    板厚2_7 = request.POST.get('板厚2-7', '')
    宽度7 = request.POST.get('宽度7', '')
    生产数量7 = request.POST.get('生产数量7', '')
    完成1_7 = request.POST.get('完成1-7', '')
    完成2_7 = request.POST.get('完成2-7', '')


    # 以上内容以确认OK
    update = UpdateSheet()
    update.user = user
    # 以下为直接调用数据库的内容
    update.部品番号 = 部品番号
    update.部品名称 = 部品名称
    update.车型 = 车型
    update.机械名 = 机械名
    update.standard_spm = standard_spm
    update.manage_num = manage_num
    update.material = material
    update.thickness = thickness
    update.container = container
    update.SNPs = SNPs

    update.标准材料宽度 = 标准材料宽度
    update.进给量 = 进给量

    update.draw_set = draw_set
    update.diehight_set = diehight_set
    update.cushion_set = cushion_set
    update.manage_pj1 = manage_pj1
    update.manage_pj2 = manage_pj2
    update.manage_pj3 = manage_pj3
    update.manage_pj4 = manage_pj4
    update.manage_pj5 = manage_pj5
    update.manage_pj6 = manage_pj6
    update.manage_pj7 = manage_pj7
    update.confirmation_meth1 = confirmation_meth1
    update.confirmation_meth2 = confirmation_meth2
    update.confirmation_meth3 = confirmation_meth3
    update.confirmation_meth4 = confirmation_meth4
    update.confirmation_meth5 = confirmation_meth5
    update.confirmation_meth6 = confirmation_meth6
    update.confirmation_meth7 = confirmation_meth7
    update.confirmation_fre1 = confirmation_fre1
    update.confirmation_fre2 = confirmation_fre2
    update.confirmation_fre3 = confirmation_fre3
    update.confirmation_fre4 = confirmation_fre4
    update.confirmation_fre5 = confirmation_fre5
    update.confirmation_fre6 = confirmation_fre6
    update.confirmation_fre7 = confirmation_fre7
    update.manage_spec1 = manage_spec1
    update.manage_spec2 = manage_spec2
    update.manage_spec3 = manage_spec3
    update.manage_spec4 = manage_spec4
    update.manage_spec5 = manage_spec5
    update.manage_spec6 = manage_spec6
    update.manage_spec7 = manage_spec7
    update.occur_day1 = occur_day1
    update.unqualified1 = unqualified1
    update.occur_reason1 = occur_reason1
    update.occur_day2 = occur_day2
    update.unqualified2 = unqualified2
    update.occur_reason2 = occur_reason2
    update.occur_day3 = occur_day3
    update.unqualified3 = unqualified3
    update.occur_reason3 = occur_reason3
    # 以下为前端页面Input的内容
    update.加工SPM = 加工SPM
    update.卷材代号 = 卷材代号
    update.拉延模压力 = 拉延模压力
    update.模具高度 = 模具高度
    update.气垫顶出高度 = 气垫顶出高度
    update.生产数 = 生产数
    update.合格数 = 合格数
    update.不良数 = 不良数
    update.模具修理 = 模具修理
    update.机械修理 = 机械修理
    update.人手替换 = 人手替换
    update.使用冲床 = 使用冲床
    update.设变号 = 设变号
    update.BL材生产日期1 = BL材生产日期1
    update.BL材生产日期2 = BL材生产日期2
    update.BL材批次号1 = BL材批次号1
    update.BL材批次号2 = BL材批次号2

    update.模具检查清扫 = 模具检查清扫
    update.加工批次号 = 加工批次号
    update.计划数量 = 计划数量

    update.初检时间 = 初检时间
    update.管理项目11 = 管理项目11
    update.管理项目12 = 管理项目12
    update.管理项目13 = 管理项目13
    update.管理项目14 = 管理项目14
    update.规格值15 = 规格值15
    update.规格值16 = 规格值16
    update.规格值17 = 规格值17
    update.二次确认1 = 二次确认1

    update.中检时间 = 中检时间
    update.中检生产数 = 中检生产数
    update.管理项目21 = 管理项目21
    update.管理项目22 = 管理项目22
    update.管理项目23 = 管理项目23
    update.管理项目24 = 管理项目24
    update.规格值25 = 规格值25
    update.规格值26 = 规格值26
    update.规格值27 = 规格值27
    update.二次确认2 = 二次确认2

    update.终检时间 = 终检时间
    update.终检生产数 = 终检生产数
    update.管理项目31 = 管理项目31
    update.管理项目32 = 管理项目32
    update.管理项目33 = 管理项目33
    update.管理项目34 = 管理项目34
    update.规格值35 = 规格值35
    update.规格值36 = 规格值36
    update.规格值37 = 规格值37
    update.二次确认3 = 二次确认3

    update.初1 = 初1
    update.中1 = 中1
    update.终1 = 终1
    update.初2 = 初2
    update.中2 = 中2
    update.终2 = 终2
    update.初3 = 初3
    update.中3 = 中3
    update.终3 = 终3

    update.检具1 = 检具1
    update.检具2 = 检具2
    update.检具3 = 检具3
    update.检具4 = 检具4
    update.检具5 = 检具5
    update.检具6 = 检具6
    update.检具7 = 检具7
    update.检具8 = 检具8

    update.初检1 = 初检1
    update.初检2 = 初检2
    update.初检3 = 初检3
    update.初检4 = 初检4
    update.初检5 = 初检5
    update.中检1 = 中检1
    update.中检2 = 中检2
    update.中检3 = 中检3
    update.中检4 = 中检4
    update.中检5 = 中检5
    update.终检1 = 终检1
    update.终检2 = 终检2
    update.终检3 = 终检3
    update.终检4 = 终检4
    update.终检5 = 终检5

    update.初检21 = 初检21
    update.初检22 = 初检22
    update.初检23 = 初检23
    update.初检24 = 初检24
    update.初检25 = 初检25
    update.中检21 = 中检21
    update.中检22 = 中检22
    update.中检23 = 中检23
    update.中检24 = 中检24
    update.中检25 = 中检25
    update.终检21 = 终检21
    update.终检22 = 终检22
    update.终检23 = 终检23
    update.终检24 = 终检24
    update.终检25 = 终检25

    update.确认点位1 = 确认点位1
    update.确认点位2 = 确认点位2
    update.作业员A = 作业员A
    update.作业员B = 作业员B
    update.作业员C = 作业员C
    update.作业员D = 作业员D
    update.备注 = 备注

    update.卷材号1 = 卷材号1
    update.板厚1_1 = 板厚1_1
    update.板厚2_1 = 板厚2_1
    update.宽度1 = 宽度1
    update.生产数量1 = 生产数量1
    update.完成1_1 = 完成1_1
    update.完成2_1 = 完成2_1

    update.卷材号2 = 卷材号2
    update.板厚1_2 = 板厚1_2
    update.板厚2_2 = 板厚2_2
    update.宽度2 = 宽度2
    update.生产数量2 = 生产数量2
    update.完成1_2 = 完成1_2
    update.完成2_2 = 完成2_2

    update.卷材号3 = 卷材号3
    update.板厚1_3 = 板厚1_3
    update.板厚2_3 = 板厚2_3
    update.宽度3 = 宽度3
    update.生产数量3 = 生产数量3
    update.完成1_3 = 完成1_3
    update.完成2_3 = 完成2_3

    update.卷材号4 = 卷材号4
    update.板厚1_4 = 板厚1_4
    update.板厚2_4 = 板厚2_4
    update.宽度4 = 宽度4
    update.生产数量4 = 生产数量4
    update.完成1_4 = 完成1_4
    update.完成2_4 = 完成2_4

    update.卷材号5 = 卷材号5
    update.板厚1_5 = 板厚1_5
    update.板厚2_5 = 板厚2_5
    update.宽度5 = 宽度5
    update.生产数量5 = 生产数量5
    update.完成1_5 = 完成1_5
    update.完成2_5 = 完成2_5

    update.卷材号6 = 卷材号6
    update.板厚1_6 = 板厚1_6
    update.板厚2_6 = 板厚2_6
    update.宽度6 = 宽度6
    update.生产数量6 = 生产数量6
    update.完成1_6 = 完成1_6
    update.完成2_6 = 完成2_6

    update.卷材号7 = 卷材号7
    update.板厚1_7 = 板厚1_7
    update.板厚2_7 = 板厚2_7
    update.宽度7 = 宽度7
    update.生产数量7 = 生产数量7
    update.完成1_7 = 完成1_7
    update.完成2_7 = 完成2_7



    # 以上内容以确认OK
    update.content_object  = model_obj
    update.save()
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    return redirect(referer)

def updatesheet_page(request, updatesheet_pk):
    updatesheet = get_object_or_404(UpdateSheet, pk=updatesheet_pk)
    manage_num_one = UpdateSheet.objects.filter(manage_num=updatesheet.manage_num).values_list("manage_num", flat=True)[0][0]
    prg_or_bl = UpdateSheet.objects.filter(部品番号=updatesheet.部品番号).values_list("部品番号", flat=True)[0][::-1][0:2]
    context = {}
    # context['preious_updatesheet'] = UpdateSheet.objects.filter(部品番号__lt=updatesheet.部品番号).last()
    # context['next_updatesheet'] = UpdateSheet.objects.filter(部品番号__gt=updatesheet.部品番号).first()
    context['updatesheet'] = updatesheet
    context['manage_num_one'] = manage_num_one
    context['prg_or_bl'] = prg_or_bl
    response = render(request,'updatesheet/updatesheet_page.html',context)
    return response

def tendencychart_list(request):
    cheeksheets_all_list = CheckSheet.objects.all()
    context = get_checksheet_list_common_data(request, cheeksheets_all_list)
    return render(request,'tendencychart/tendencychart_list.html',context)

def tendencychart_page(request, checksheet_pk):
    checksheet = get_object_or_404(CheckSheet, pk=checksheet_pk)
    prg_or_bl = CheckSheet.objects.filter(parts_code=checksheet.parts_code).values_list("parts_code", flat=True)[0][::-1][0:2]
    manage_num_one = CheckSheet.objects.filter(parts_code=checksheet.parts_code).values_list("管理编号", flat=True)[0][0]

    checkpoint = UpdateSheet.objects.filter(部品番号=checksheet.parts_code).values_list("确认点位2", flat=True)[0]
    # updatesheet = UpdateSheet.objects.all()
    checktime = UpdateSheet.objects.filter(部品番号=checksheet.parts_code).values_list("updated_time", flat=True)
    checkdata1 = UpdateSheet.objects.filter(部品番号=checksheet.parts_code).values_list("终检1", flat=True)
    checkdata2 = UpdateSheet.objects.filter(部品番号=checksheet.parts_code).values_list("终检2", flat=True)
    checkdata3 = UpdateSheet.objects.filter(部品番号=checksheet.parts_code).values_list("终检3", flat=True)
    checkdata4 = UpdateSheet.objects.filter(部品番号=checksheet.parts_code).values_list("终检4", flat=True)
    checkdata5 = UpdateSheet.objects.filter(部品番号=checksheet.parts_code).values_list("终检5", flat=True)

    checkdata21 = UpdateSheet.objects.filter(部品番号=checksheet.parts_code).values_list("终检21", flat=True)
    checkdata22 = UpdateSheet.objects.filter(部品番号=checksheet.parts_code).values_list("终检22", flat=True)
    checkdata23 = UpdateSheet.objects.filter(部品番号=checksheet.parts_code).values_list("终检23", flat=True)
    checkdata24 = UpdateSheet.objects.filter(部品番号=checksheet.parts_code).values_list("终检24", flat=True)
    checkdata25 = UpdateSheet.objects.filter(部品番号=checksheet.parts_code).values_list("终检25", flat=True)
    # first_check = UpdateSheet.objects.values("初检1")

    try:
        点检时间1 = checktime[0]
    except:
        点检时间1 = None
    try:
        点检时间2 = checktime[1]
    except:
        点检时间2 = None
    try:
        点检时间3 = checktime[2]
    except:
        点检时间3 = None
    try:
        点检时间4 = checktime[3]
    except:
        点检时间4 = None
    try:
        点检时间5 = checktime[4]
    except:
        点检时间5 = None
    try:
        点检时间6 = checktime[5]
    except:
        点检时间6 = None
    try:
        点检时间7 = checktime[6]
    except:
        点检时间7 = None
    try:
        点检时间8 = checktime[7]
    except:
        点检时间8 = None
    try:
        点检时间9 = checktime[8]
    except:
        点检时间9 = None
    try:
        点检时间10 = checktime[9]
    except:
        点检时间10 = None

    try:
        终检01 = float(checkdata1[0])
    except:
        终检01 = 3.0
    try:
        终检11 = float(checkdata1[1])
    except:
        终检11 = 3.0
    try:
        终检21 = float(checkdata1[2])
    except:
        终检21 = 3.0
    try:
        终检31 = float(checkdata1[3])
    except:
        终检31 = 3.0
    try:
        终检41 = float(checkdata1[4])
    except:
        终检41 = 3.0
    try:
        终检51 = float(checkdata1[5])
    except:
        终检51 = 3.0
    try:
        终检61 = float(checkdata1[6])
    except:
        终检61 = 3.0
    try:
        终检71 = float(checkdata1[7])
    except:
        终检71 = 3.0
    try:
        终检81 = float(checkdata1[8])
    except:
        终检81 = 3.0
    try:
        终检91 = float(checkdata1[9])
    except:
        终检91 = 3.0

    try:
        终检201 = float(checkdata2[0])
    except:
        终检201 = 3.0
    try:
        终检211 = float(checkdata2[1])
    except:
        终检211 = 3.0
    try:
        终检221 = float(checkdata2[2])
    except:
        终检221 = 3.0
    try:
        终检231 = float(checkdata2[3])
    except:
        终检231 = 3.0
    try:
        终检241 = float(checkdata2[4])
    except:
        终检241 = 3.0
    try:
        终检251 = float(checkdata2[5])
    except:
        终检251 = 3.0
    try:
        终检261 = float(checkdata2[6])
    except:
        终检261 = 3.0
    try:
        终检271 = float(checkdata2[7])
    except:
        终检271 = 3.0
    try:
        终检281 = float(checkdata2[8])
    except:
        终检281 = 3.0
    try:
        终检291 = float(checkdata2[9])
    except:
        终检291 = 3.0

    try:
        终检301 = float(checkdata3[0])
    except:
        终检301 = 3.0
    try:
        终检311 = float(checkdata3[1])
    except:
        终检311 = 3.0
    try:
        终检321 = float(checkdata3[2])
    except:
        终检321 = 3.0
    try:
        终检331 = float(checkdata2[3])
    except:
        终检331 = 3.0
    try:
        终检341 = float(checkdata3[4])
    except:
        终检341 = 3.0
    try:
        终检351 = float(checkdata3[5])
    except:
        终检351 = 3.0
    try:
        终检361 = float(checkdata3[6])
    except:
        终检361 = 3.0
    try:
        终检371 = float(checkdata3[7])
    except:
        终检371 = 3.0
    try:
        终检381 = float(checkdata3[8])
    except:
        终检381 = 3.0
    try:
        终检391 = float(checkdata3[9])
    except:
        终检391 = 3.0

    try:
        终检401 = float(checkdata4[0])
    except:
        终检401 = 3.0
    try:
        终检411 = float(checkdata4[1])
    except:
        终检411 = 3.0
    try:
        终检421 = float(checkdata4[2])
    except:
        终检421 = 3.0
    try:
        终检431 = float(checkdata4[3])
    except:
        终检431 = 3.0
    try:
        终检441 = float(checkdata4[4])
    except:
        终检441 = 3.0
    try:
        终检451 = float(checkdata4[5])
    except:
        终检451 = 3.0
    try:
        终检461 = float(checkdata4[6])
    except:
        终检461 = 3.0
    try:
        终检471 = float(checkdata4[7])
    except:
        终检471 = 3.0
    try:
        终检481 = float(checkdata4[8])
    except:
        终检481 = 3.0
    try:
        终检491 = float(checkdata4[9])
    except:
        终检491 = 3.0


    try:
        终检501 = float(checkdata5[0])
    except:
        终检501 = 3.0
    try:
        终检511 = float(checkdata5[1])
    except:
        终检511 = 3.0
    try:
        终检521 = float(checkdata5[2])
    except:
        终检521 = 3.0
    try:
        终检531 = float(checkdata5[3])
    except:
        终检531 = 3.0
    try:
        终检541 = float(checkdata5[4])
    except:
        终检541 = 3.0
    try:
        终检551 = float(checkdata5[5])
    except:
        终检551 = 3.0
    try:
        终检561 = float(checkdata5[6])
    except:
        终检561 = 3.0
    try:
        终检571 = float(checkdata5[7])
    except:
        终检571 = 3.0
    try:
        终检581 = float(checkdata5[8])
    except:
        终检581 = 3.0
    try:
        终检591 = float(checkdata5[9])
    except:
        终检591 = 3.0

    try:
        终检2101 = float(checkdata21[0])
    except:
        终检2101 = 3.0
    try:
        终检2111 = float(checkdata21[1])
    except:
        终检2111 = 3.0
    try:
        终检2121 = float(checkdata21[2])
    except:
        终检2121 = 3.0
    try:
        终检2131 = float(checkdata21[3])
    except:
        终检2131 = 3.0
    try:
        终检2141 = float(checkdata21[4])
    except:
        终检2141 = 3.0
    try:
        终检2151 = float(checkdata21[5])
    except:
        终检2151 = 3.0
    try:
        终检2161 = float(checkdata21[6])
    except:
        终检2161 = 3.0
    try:
        终检2171 = float(checkdata21[7])
    except:
        终检2171 = 3.0
    try:
        终检2181 = float(checkdata21[8])
    except:
        终检2181 = 3.0
    try:
        终检2191 = float(checkdata21[9])
    except:
        终检2191 = 3.0

    try:
        终检2201 = float(checkdata22[0])
    except:
        终检2201 = 3.0
    try:
        终检2211 = float(checkdata22[1])
    except:
        终检2211 = 3.0
    try:
        终检2221 = float(checkdata22[2])
    except:
        终检2221 = 3.0
    try:
        终检2231 = float(checkdata22[3])
    except:
        终检2231 = 3.0
    try:
        终检2241 = float(checkdata22[4])
    except:
        终检2241 = 3.0
    try:
        终检2251 = float(checkdata22[5])
    except:
        终检2251 = 3.0
    try:
        终检2261 = float(checkdata22[6])
    except:
        终检2261 = 3.0
    try:
        终检2271 = float(checkdata22[7])
    except:
        终检2271 = 3.0
    try:
        终检2281 = float(checkdata22[8])
    except:
        终检2281 = 3.0
    try:
        终检2291 = float(checkdata22[9])
    except:
        终检2291 = 3.0

    try:
        终检2301 = float(checkdata23[0])
    except:
        终检2301 = 3.0
    try:
        终检2311 = float(checkdata23[1])
    except:
        终检2311 = 3.0
    try:
        终检2321 = float(checkdata23[2])
    except:
        终检2321 = 3.0
    try:
        终检2331 = float(checkdata23[3])
    except:
        终检2331 = 3.0
    try:
        终检2341 = float(checkdata23[4])
    except:
        终检2341 = 3.0
    try:
        终检2351 = float(checkdata23[5])
    except:
        终检2351 = 3.0
    try:
        终检2361 = float(checkdata23[6])
    except:
        终检2361 = 3.0
    try:
        终检2371 = float(checkdata23[7])
    except:
        终检2371 = 3.0
    try:
        终检2381 = float(checkdata32[8])
    except:
        终检2381 = 3.0
    try:
        终检2391 = float(checkdata23[9])
    except:
        终检2391 = 3.0

    try:
        终检2401 = float(checkdata24[0])
    except:
        终检2401 = 3.0
    try:
        终检2411 = float(checkdata24[1])
    except:
        终检2411 = 3.0
    try:
        终检2421 = float(checkdata24[2])
    except:
        终检2421 = 3.0
    try:
        终检2431 = float(checkdata24[3])
    except:
        终检2431 = 3.0
    try:
        终检2441 = float(checkdata24[4])
    except:
        终检2441 = 3.0
    try:
        终检2451 = float(checkdata24[5])
    except:
        终检2451 = 3.0
    try:
        终检2461 = float(checkdata24[6])
    except:
        终检2461 = 3.0
    try:
        终检2471 = float(checkdata24[7])
    except:
        终检2471 = 3.0
    try:
        终检2481 = float(checkdata24[8])
    except:
        终检2481 = 3.0
    try:
        终检2491 = float(checkdata24[9])
    except:
        终检2491 = 3.0

    try:
        终检2501 = float(checkdata25[0])
    except:
        终检2501 = 3.0
    try:
        终检2511 = float(checkdata25[1])
    except:
        终检2511 = 3.0
    try:
        终检2521 = float(checkdata25[2])
    except:
        终检2521 = 3.0
    try:
        终检2531 = float(checkdata25[3])
    except:
        终检2531 = 3.0
    try:
        终检2541 = float(checkdata25[4])
    except:
        终检2541 = 3.0
    try:
        终检2551 = float(checkdata25[5])
    except:
        终检2551 = 3.0
    try:
        终检2561 = float(checkdata25[6])
    except:
        终检2561 = 3.0
    try:
        终检2571 = float(checkdata25[7])
    except:
        终检2571 = 3.0
    try:
        终检2581 = float(checkdata25[8])
    except:
        终检2581 = 3.0
    try:
        终检2591 = float(checkdata25[9])
    except:
        终检2591 = 3.0

    context = {}
    # context['preious_tendencychart'] = CheckSheet.objects.filter(parts_code__lt=tendencychart.parts_code).last()
    # context['next_tendencychart'] = CheckSheet.objects.filter(parts_code__gt=tendencychart.parts_code).first()
    context['checksheet'] = checksheet
    context['checkpoint'] = checkpoint
    # context['checktime'] = checktime
    # context['checktime'] = checktime
    context['点检时间1'] = 点检时间1
    context['点检时间2'] = 点检时间2
    context['点检时间3'] = 点检时间3
    context['点检时间4'] = 点检时间4
    context['点检时间5'] = 点检时间5
    context['点检时间6'] = 点检时间6
    context['点检时间7'] = 点检时间7
    context['点检时间8'] = 点检时间8
    context['点检时间9'] = 点检时间9
    context['点检时间10'] = 点检时间10

    context['终检01'] = 终检01
    context['终检11'] = 终检11
    context['终检21'] = 终检21
    context['终检31'] = 终检31
    context['终检41'] = 终检41
    context['终检51'] = 终检51
    context['终检61'] = 终检61
    context['终检71'] = 终检71
    context['终检81'] = 终检81
    context['终检91'] = 终检91

    context['终检201'] = 终检201
    context['终检211'] = 终检211
    context['终检221'] = 终检221
    context['终检231'] = 终检231
    context['终检241'] = 终检241
    context['终检251'] = 终检251
    context['终检261'] = 终检261
    context['终检271'] = 终检271
    context['终检281'] = 终检281
    context['终检291'] = 终检291

    context['终检301'] = 终检301
    context['终检311'] = 终检311
    context['终检321'] = 终检321
    context['终检331'] = 终检331
    context['终检341'] = 终检341
    context['终检351'] = 终检351
    context['终检361'] = 终检361
    context['终检371'] = 终检371
    context['终检381'] = 终检381
    context['终检391'] = 终检391

    context['终检401'] = 终检401
    context['终检411'] = 终检411
    context['终检421'] = 终检421
    context['终检431'] = 终检431
    context['终检441'] = 终检441
    context['终检451'] = 终检451
    context['终检461'] = 终检461
    context['终检471'] = 终检471
    context['终检481'] = 终检481
    context['终检491'] = 终检491

    context['终检501'] = 终检501
    context['终检511'] = 终检511
    context['终检521'] = 终检521
    context['终检531'] = 终检531
    context['终检541'] = 终检541
    context['终检551'] = 终检551
    context['终检561'] = 终检561
    context['终检571'] = 终检571
    context['终检581'] = 终检581
    context['终检591'] = 终检591

    context['终检2101'] = 终检2101
    context['终检2111'] = 终检2111
    context['终检2121'] = 终检2121
    context['终检2131'] = 终检2131
    context['终检2141'] = 终检2141
    context['终检2151'] = 终检2151
    context['终检2161'] = 终检2161
    context['终检2171'] = 终检2171
    context['终检2181'] = 终检2181
    context['终检2191'] = 终检2191

    context['终检2201'] = 终检2201
    context['终检2211'] = 终检2211
    context['终检2221'] = 终检2221
    context['终检2231'] = 终检2231
    context['终检2241'] = 终检2241
    context['终检2251'] = 终检2251
    context['终检2261'] = 终检2261
    context['终检2271'] = 终检2271
    context['终检2281'] = 终检2281
    context['终检2291'] = 终检2291

    context['终检2301'] = 终检2301
    context['终检2311'] = 终检2311
    context['终检2321'] = 终检2321
    context['终检2331'] = 终检2331
    context['终检2341'] = 终检2341
    context['终检2351'] = 终检2351
    context['终检2361'] = 终检2361
    context['终检2371'] = 终检2371
    context['终检2381'] = 终检2381
    context['终检2391'] = 终检2391

    context['终检2401'] = 终检2401
    context['终检2411'] = 终检2411
    context['终检2421'] = 终检2421
    context['终检2431'] = 终检2431
    context['终检2441'] = 终检2441
    context['终检2451'] = 终检2451
    context['终检2461'] = 终检2461
    context['终检2471'] = 终检2471
    context['终检2481'] = 终检2481
    context['终检2491'] = 终检2491

    context['终检2501'] = 终检2501
    context['终检2511'] = 终检2511
    context['终检2521'] = 终检2521
    context['终检2531'] = 终检2531
    context['终检2541'] = 终检2541
    context['终检2551'] = 终检2551
    context['终检2561'] = 终检2561
    context['终检2571'] = 终检2571
    context['终检2581'] = 终检2581
    context['终检2591'] = 终检2591

    context['prg_or_bl'] = prg_or_bl

    response = render(request,'tendencychart/tendencychart_page.html',context)
    return response

def search2(request):
    search_words = request.GET.get('wd', '')
    # 筛选：搜索
    search_checksheets = CheckSheet.objects.filter(parts_code__icontains=search_words)

    # 分页
    paginator = Paginator(search_checksheets, 10)
    page_num = request.GET.get('page', 1)  #获取url的页面参数（GET请求）
    page_of_checksheets = paginator.get_page(page_num)

    context = {}
    context['search_words'] = search_words
    context['search_checksheets_count'] = search_checksheets.count()
    context['page_of_checksheets'] = page_of_checksheets
    return render(request, 'tendencychart/search2.html', context)