from django.db import models
from worker.models import *


class Vacancy(models.Model):
    view = models.ManyToManyField(User)
    tittle = models.CharField(max_length=255)
    salary = models.IntegerField(null=True, blank=True)
    description = models.TextField(default='Нет описания')
    is_relevant = models.BooleanField(default=True)
    email = models.EmailField()
    contacts = models.CharField(max_length=100, verbose_name='Контакты')
    candidate = models.ManyToManyField(
        to=Worker,
        blank=True,
    )
    category = models.ForeignKey(
        to="Category",
        null=True, blank=True,
        on_delete=models.SET_NULL,
        verbose_name='category'
    )

    def __str__(self):
        return self.tittle

    class Meta:
        verbose_name = 'Вакансии'
        verbose_name_plural = 'Вакансия'
        ordering = ['salary']


class Category(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
