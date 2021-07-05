from django.shortcuts import render, get_object_or_404
from django.db.models import Sum
from django.core.paginator import Paginator

from checksheet.models import UpdateSheet

def home(request):
    context = {}
    return render(request,'home.html',context)

def search(request):
    search_words = request.GET.get('wd', '')
    # 分词：按空格 & | ~
    # for word in search_words.split(' '):
    #     if condition in None:
    #         condition = Q(部品番号__icontains=word)
    #     else:
    #         condition = condition | Q(部品番号__icontains=word)

    # search_words = []
    # if condition in not None:
    #     # 筛选：搜索
    #     search_updatesheets = UpdateSheet.objects.filter(condition)

    # 筛选：搜索
    search_updatesheets = UpdateSheet.objects.filter(部品番号__icontains=search_words)

    # 分页
    paginator = Paginator(search_updatesheets, 10)
    page_num = request.GET.get('page', 1)  #获取url的页面参数（GET请求）
    page_of_updatesheets = paginator.get_page(page_num)

    context = {}
    context['search_words'] = search_words
    context['search_updatesheets_count'] = search_updatesheets.count()
    context['page_of_updatesheets'] = page_of_updatesheets
    return render(request, 'search.html', context)