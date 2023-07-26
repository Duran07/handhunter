from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Recruiter


def recruiter_list(request):
    recruiters = Recruiter.objects.all()
    context = {'recruiters': recruiters}
    return render(request, 'recruit/list.html', context)


def recruiter_detail(request, pk):
    recruiter_object = Recruiter.objects.get(pk=pk)
    context = {'recruiter_object': recruiter_object}
    return render(
        request,
        'recruit/detail.html',
        {'recruiter_object': recruiter_object}
    )


class RecruitView(View):
    def get(self, request):
        recruiters = Recruiter.objects.all()
        return render(request, 'recruit/list.html', {'recruiters': recruiters})


class RecruitListView(LoginRequiredMixin, ListView):
    model = Recruiter


class RecruiterCreateView(CreateView):
    model = Recruiter
    fields = '__all__'
    success_url = reverse_lazy('recruiter-list')


class RecruiterEditView(UpdateView):
    model = Recruiter
    fields = '__all__'
    template_name = 'recruit/edit.html'
    success_url = reverse_lazy('recruiter-list')
