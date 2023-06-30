from django.shortcuts import render
from .models import *


def worker(request):
    worker_office = Worker.objects.all()
    return render(request, "workers.html", {'workers': worker_office})


def worker_info(request, id):
    worker_object = Worker.objects.get(id=id)
    # (sql) SELECT * FROM Worker id={id}
    context = {"worker": worker_object}
    return render(request, 'worker.html', context)


def resume_list(request):
    resume_query = Resume.objects.all()
    context = {"resumes": resume_query}
    return render(request, 'resume/resume_list.html')


def resume_info(request, id):
    resume_object = Resume.objects.get(id=id)
    context = {'resume': resume_object}

    return render(request, 'resume/resume_detail.html')


def my_resume(request):
    resume_query = Resume.objects.filter(worker=request.user.worker)
    # resume_query = request.user.worker.resume.all()
    context = {"resumes": resume_query}
    return render(request, 'resume/resume_list.html')
