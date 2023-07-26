from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import *


def worker(request):
    worker_office = Worker.objects.all()
    return render(request, "workers.html", {'workers': worker_office})


def worker_info(request, id):
    worker_object = Worker.objects.get(id=id)
    # (sql) SELECT * FROM Worker id={id}
    context = {"worker": worker_object}
    return render(request, 'worker.html', context)


def resume_list(request):
    resumes = Resume.objects.all()
    context = {"resumes": resumes}
    return render(request, 'resume/resume_list.html', context)


def resume_info(request, id):
    resume_object = Resume.objects.get(id=id)

    return render(request, 'resume/resume_detail.html', {'resume': resume_object})


def resume_edit(request, id):
    resume_object = Resume.objects.get(id=id)

    if request.method == "GET":
        form = ResumeEditForm(instance=resume_object)
        return render(request, "resume/resume_edit.html", {"form": form})

    elif request.method == "POST":
        form = ResumeEditForm(data=request.POST, instance=resume_object, files=request.FILES)
        if form.is_valid():
            obj = form.save()
            return redirect(resume_info, id=obj.id)
        else:
            return HttpResponse("Форма неправильно заполнено")


def my_resume(request):
    if request.user.is_authenticated:
        resume_query = Resume.objects.filter(worker=request.user.worker)
        # resume_query = request.user.worker.resume.all()
        context = {"resumes": resume_query}
        return render(request, 'resume/resume_list.html')
    else:
        return redirect('home')


def add_resume(request):
    if request.method == "POST":
        form = ResumeCreateForm(request.POST)
        if form.is_valid():
            new_resume = form.save(commit=False)
            new_resume.worker = request.user.worker
            new_resume.save()
            return redirect(f'/resume-info/{new_resume.id}/')
    form = ResumeCreateForm()
    return render(request, 'resume/resume_add.html', {"form": form})


def create_company(request):
    if request.method == "POST":
        form = CompanyCreateForm(request.POST)
        if form.is_valid():
            new_company = form.save(commit=False)
            new_company.worker = request.user.worker
            new_company.save()
            return redirect(f"/company-info/{new_company.id}")
    cc_form = CompanyCreateForm()
    return render(request, 'company/create_form.html', {"cc_form": cc_form})


def company_info(request, id):
    company_obj = Company.objects.get(id=id)
    context = {"company": company_obj}
    return render(request, 'company/company_info.html', context)


def company_list(request):
    companies = Company.objects.all()
    context = {"companies": companies}
    return render(request, 'company/company_list.html')


def company_edit(request, id):
    company = Company.objects.get(id=id)

    if request.method == "GET":
        form = CompanyCreateForm(instance=company)
        return render(request, "company/company_edit.html", {"form": form})

    elif request.method == "POST":
        company_object = CompanyCreateForm(data=request.POST, instance=company)
        if company_object.is_valid():
            obj = company_object.save()
            return redirect(company_list, id=obj.id)
        return HttpResponse("Форма неправильно заполнено")
