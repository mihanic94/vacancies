from django.db import models
from django.urls import reverse


class Company(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    location = models.CharField(max_length=50, verbose_name='город')
    logo = models.URLField(default='https://place-hold.it/100x60', verbose_name='логотип')
    description = models.TextField(verbose_name='описание')
    employee_count = models.PositiveIntegerField(verbose_name='количество сотрудников')

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company', args=[self.pk])


class Specialty(models.Model):
    code = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='код')
    title = models.CharField(max_length=50, verbose_name='название')
    picture = models.URLField(default='https://place-hold.it/100x60', verbose_name='изображение')

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('specialty', args=[self.code])


class Vacancy(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    specialty = models.ForeignKey(
        Specialty,
        on_delete=models.PROTECT,
        related_name='vacancies',
        verbose_name='специализация',
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='vacancies',
        verbose_name='компания',
    )
    skills = models.TextField(verbose_name='навыки')
    description = models.TextField(verbose_name='описание')
    salary_min = models.PositiveIntegerField(verbose_name='минимальная зарплата')
    salary_max = models.PositiveIntegerField(verbose_name='максимальная зарплата')
    published_at = models.DateField(verbose_name='дата публикации')

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('vacancy', args=[self.pk])
