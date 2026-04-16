# home/views.py
from django.shortcuts import render
from .models import HeroSlider, About, ResearchHighlight


def home_view(request):
    sliders = HeroSlider.objects.filter(is_active=True)
    about = About.load()
    research = ResearchHighlight.objects.all()

    return render(request, 'home/index.html', {
        'sliders': sliders,
        'about': about,
        'research': research,
    })