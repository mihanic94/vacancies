from django.http import HttpResponseNotFound, HttpResponseServerError
from django.views.generic import ListView, DetailView

from vacancies.models import Company, Vacancy, Specialty


class VacanciesHomeView(ListView):
    model = Specialty
    template_name = 'vacancies/index.html'


class AllVacanciesView(ListView):
    model = Vacancy
    template_name = 'vacancies/vacancies.html'



class VacanciesSpecialty(ListView):
    model = Vacancy
    template_name = 'vacancies/vacancies.html'


class CompanyView(DetailView):
    model = Company
    template_name = 'vacancies/company.html'


class VacancyView(DetailView):
    model = Vacancy
    template_name = 'vacancies/vacancy.html'


def page_not_found(request, exception):
    return HttpResponseNotFound('По данному адресу страницы не существует!')


def server_error(request):
    return HttpResponseServerError('Простите, извините...у нас что-то поломалось!')
