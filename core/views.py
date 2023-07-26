from django.shortcuts import render, HttpResponse, redirect
from .models import Vacancy
from django.contrib.auth.models import User
from .forms import *


def homepage(request):
    return render(request=request, template_name="index.html")


def about_us(request):
    return HttpResponse("Работник мечты")


def information(request):
    return HttpResponse('''
        <div>
            Phone: +996777123456 <br>
            Email: office@handhunter.kg
        <div>
    ''')


def vacancy_list(request):
    min_experience = request.GET.get('min_experience')
    max_experience = request.GET.get('max_experience')
    employment_type = request.GET.get('employment_type')
    skill_query = request.GET.get('skills')
    vacancies = Vacancy.objects.all()
    if min_experience:
        vacancies = vacancies.filter(EXPERIENCE__gte=min_experience)
    if max_experience:
        vacancies = vacancies.filter(EXPERIENCE__lte=max_experience)
    if employment_type:
        vacancies = vacancies.filter(job_time=employment_type)
    if skill_query:
        vacancies = vacancies.filter(skills__name__icontains=skill_query)
    vacancies = Vacancy.objects.all()
    context = {"vacancies": vacancies}
    context["example"] = "hello world"
    return render(request, 'vacancies.html', context)


def vacancy_detail(request, id):
    vacancy_object = Vacancy.objects.get(id=id)
    candidates = vacancy_object.candidate.all()
    context = {
        'vacancy': vacancy_object,
        'candidates': candidates,
    }
    return render(request, 'vacancy/vacancy_page.html', context)


def search(request):
    word = request.GET["keyword"]
    vacancy_list = Vacancy.objects.filter(title__contains=word)
    context = {"vacancies": vacancy_list}
    return render(request, 'vacancies.html', context)


def reg_view(request):
    if request.method == "POST":
        user = User(
            username=request.POST["username"]
        )
        user.save()
        user.set_password(request.POST["password"])
        user.save()
        return HttpResponse("Готово")

    return render(
        request,
        "auth/registr.html"
    )


def vacancy_add(request):
    if request.method == "POST":
        new_vacancy = Vacancy(
            title=request.POST["title"],
            salary=int(request.POST["salary"]),
            description=request.POST["description"],
            email=request.POST["email"],
            contacts=request.POST["contacts"],
        )
        new_vacancy.save()
        return redirect(f'/vacancy/{new_vacancy.id}/')
    return render(request, 'vacancy/vacancy_form.html')


def vacancy_edit(request, id):
    vacancy = Vacancy.objects.get(id=id)

    if request.method == "GET":
        form = VacancyEditForm(instance=vacancy)
        return render(request, "vacancy/vacancy_edit_form.html", {"form": form})

    elif request.method == "POST":
        object_vac = VacancyEditForm(data=request.POST, instance=vacancy)
        if object_vac.is_valid():
            vacancies = object_vac.save()
            return redirect(vacancy_list, id=vacancies.id)
        return HttpResponse("Форма не валидна")


def vacancy_add_via_django_form(request):
    if request.method == "POST":
        form = VacancyForm(request.POST)
        if form.is_valid():
            new_vacancy = form.save()
            return redirect(f'/vacancy/{new_vacancy.id}/')
    vacancy_form = VacancyForm()
    return render(
        request,
        'vacancy/vacancy_django_form.html',
        {"vacancy_form": vacancy_form}
    )
