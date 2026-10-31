from django.db import models
from datetime import date, timedelta




class Project(models.Model):
    name = models.CharField(max_length=200, verbose_name="Ім'я")
    description = models.CharField(max_length=200, verbose_name="Опис")
    tech = models.TextField(verbose_name="Технологія")
    date = models.DateField(auto_now_add=True, verbose_name="Дата реєстрації")
    picure = models.ImageField(verbose_name="Фото проєкту")
    gitHub = models.URLField(max_length=200, verbose_name="Посилання на проєкт")

    def __str__(self):
        return self.name




class Skill(models.Model):
    name = models.CharField(max_length=200, verbose_name="Ім'я")
    lvlpossesses = models.IntegerField(verbose_name="Від 1 до 10")
    category = models.CharField(max_length=200, verbose_name="Категорія")

    def __str__(self):
        return self.name





class Expirience(models.Model):
    position = models.CharField(max_length=200, verbose_name="Ім'я")
    company = models.CharField(max_length=200, verbose_name="Назва")
    period = models.DateField(auto_now_add=True, verbose_name="Період роботи")
    description = models.CharField(max_length=200, verbose_name="Опис")



    def __str__(self):
        return f"{self.position} - {self.company}"

















# Create your models here.
