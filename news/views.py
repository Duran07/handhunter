from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse_lazy


def news_list(request):
    news = ArticleNew.objects.all()
    context = {"news_object": news}
    return render(request, "news/news_list.html", context)


def detail_news(request, pk):
    news_object = ArticleNew.objects.get(pk=pk)
    return render(
        request,
        'news/detail.html',
        {'news': news_object}
    )


class NewsCreateView(CreateView):
    model = ArticleNew
    fields = '__all__'
    success_url = reverse_lazy('news-list')


class NewsEditView(UpdateView):
    model = ArticleNew
    fields = '__all__'
    template_name = 'news/edit.html'
    success_url = reverse_lazy('news-list')


class AuctionItemDetailView(DetailView):
    model = ArticleNew

    def get_object(self, queryset=None):
        item = super().get_object(queryset)
        item.views_count += 1
        item.save()
        return item


