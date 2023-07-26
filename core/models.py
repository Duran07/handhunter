from django.db import models
from worker.models import *
from django.contrib.auth.models import User



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
    skills = models.ManyToManyField(to=Skill)
    EXPERIENCE = models.IntegerField(null=True, blank=True)
    part_job = "частичный рабочий день"
    full_job = "полный рабочий день"
    place_job = "сдельная работа"
    job_time_choices = [
        (part_job, "part_job"),
        (full_job, "full_job"),
        (place_job, "place_job"),
    ]
    job_time = models.CharField(
        max_length=200,
        choices=job_time_choices,
        default=part_job
    )

    def is_upperclass(self):
        return self.job_time in {self.full_job, self.place_job}

    def __str__(self):
        return self.tittle

    class Meta:
        verbose_name = 'Вакансии'
        verbose_name_plural = 'Вакансия'
        ordering = ['salary']


class Skill(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField(default='Нет описания')
    email = models.EmailField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
