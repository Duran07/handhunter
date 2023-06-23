from django.shortcuts import render
from .models import Worker


def worker(request):
    return render(request=request, template_name='worker.html')

