from django.shortcuts import render
from .models import Worker


def worker(request):
    worker_office = Worker.objects.all()
    return render(request, "workers.html", {'workers': worker_office})


def worker_info(request, id):
    worker_object = Worker.objects.get(id=id)
    #(sql) SELECT * FROM Worker id={id}
    context = {"worker": worker_object}
    return render(request, 'worker.html', context)

