from django.db import models


class Worker(models.Model):
    name = models.TextField(max_length=900, verbose_name="ФИО")
    specialization = models.CharField(max_length=64, verbose_name="Специализация")
    an_expect_salary = models.IntegerField(verbose_name="ожидаемая зарплата")
    is_searching = models.BooleanField(default=True, verbose_name="Ожидаемая зарплата")

    def __str__(self):
        return self.name
