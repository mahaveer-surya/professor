# alumni/views.py
from django.shortcuts import render
from .models import Alumni


def alumni_list(request):
    current_alumni = Alumni.objects.filter(
        category='current', is_active=True
    )

    passed_alumni = Alumni.objects.filter(
        category='passed', is_active=True
    ).order_by('-passing_year')

    return render(request, 'alumni/alumni_list.html', {
        'current_alumni': current_alumni,
        'passed_alumni': passed_alumni,
    })