# news/views.py
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import News


def news_list(request):
    news_items = News.objects.filter(is_active=True)

    paginator = Paginator(news_items, 6)  # 6 cards per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'news/news_list.html', {
        'page_obj': page_obj
    })