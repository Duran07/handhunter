from django.shortcuts import render, HttpResponse
from .models import Vacancy


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
    vacancies = Vacancy.objects.all()
    context = {"vacancies": vacancies}
    context["example"] = "hello world"
    return render(request, 'vacancies.html', context)





