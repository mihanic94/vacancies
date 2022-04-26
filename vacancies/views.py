from django.http import HttpResponseNotFound, HttpResponseServerError, Http404
from django.views.generic import ListView, DetailView

from vacancies.models import Company, Vacancy, Specialty


class VacanciesHomeView(ListView):
    model = Specialty
    template_name = 'vacancies/index.html'
    context_object_name = 'specialties'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['companies'] = Company.objects.all()
        return context


class AllVacanciesView(ListView):
    model = Vacancy
    template_name = 'vacancies/vacancies.html'
    context_object_name = 'vacancies'
    extra_context = {'title': 'Все вакансии'}


class VacanciesSpecialty(ListView):
    model = Vacancy
    template_name = 'vacancies/vacancies.html'
    context_object_name = 'vacancies'

    def get_queryset(self):
        return Vacancy.objects.filter(specialty__code=self.kwargs['specialty_code'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['title'] = Specialty.objects.get(code=self.kwargs['specialty_code']).title
        except Exception:
            raise Http404
        return context


class CompanyView(ListView):
    model = Vacancy
    template_name = 'vacancies/company.html'
    context_object_name = 'vacancies'

    def get_queryset(self):
        return Vacancy.objects.filter(company_id=self.kwargs['company_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=self.kwargs['company_id'])
        except Exception:
            raise Http404
        return context


class VacancyView(DetailView):
    model = Vacancy
    template_name = 'vacancies/vacancy.html'
    pk_url_kwarg = 'vacancy_id'
    context_object_name = 'vacancy'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = super().get_object().company
        context['specialty'] = super().get_object().specialty
        return context


def page_not_found(request, exception):
    return HttpResponseNotFound('По данному адресу страницы не существует!')


def server_error(request):
    return HttpResponseServerError('Простите, извините...у нас что-то поломалось!')
