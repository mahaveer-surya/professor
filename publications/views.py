# publications/views.py
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Publication

def publication_list(request):
    publications = Publication.objects.all()

    paginator = Paginator(publications, 10)  # 10 per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'publications/publication_list.html', {
        'page_obj': page_obj
    })