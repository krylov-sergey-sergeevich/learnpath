from django.shortcuts import render

from .models import Material


def index_view(request):
    materials = Material.objects.all()
    return render(request, 'materials/index.html', {'materials': materials})
