from django.db import models


class Vacancy(models.Model):
    tittle = models.CharField(max_length=255)
    salary = models.IntegerField(null=True, blank=True)
    description = models.TextField(default='Нет описания')
    is_relevant = models.BooleanField(default=True)
    email = models.EmailField()
    contacts = models.CharField(max_length=100, verbose_name='Контакты')

    def __str__(self):
        return self.tittle


class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(max_length=700)
    worker_number = models.IntegerField(null=True)
    is_hunting = models.BooleanField(default=True)

    def __str__(self):
        return self.name
