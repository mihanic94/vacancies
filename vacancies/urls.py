from django.urls import path

from vacancies.views import VacanciesHomeView, AllVacanciesView, VacanciesSpecialty, CompanyView, VacancyView

urlpatterns = [
    path('', VacanciesHomeView.as_view(), name='home'),
    path('vacancies/', AllVacanciesView.as_view(), name='all_vacancies'),
    path('vacancies/cat/<slug:specialty_code>/', VacanciesSpecialty.as_view(), name='specialty'),
    path('companies/<int:company_id>', CompanyView.as_view(), name='company'),
    path('vacancies/<int:vacancy_id>/', VacancyView.as_view(), name='vacancy'),
]