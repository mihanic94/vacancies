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
