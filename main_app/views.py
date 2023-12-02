from django.shortcuts import render
from .models import Dmodels
from django.views.generic import DetailView

def home_page(request):
    return render(request, 'index.html')

def models_3d(request):
    data = Dmodels.objects.all()
    context = {
        'data': data
    }
    return render(request, 'team.html', context)

class DetailModel(DetailView):
    model = Dmodels
    template_name = 'detail.html'