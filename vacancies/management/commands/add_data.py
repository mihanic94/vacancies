from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        from vacancies.models import Company, Specialty, Vacancy
        from vacancies.data import jobs, companies, specialties
        from datetime import date

        for company in companies:
            company_instance = Company()
            company_instance.name = company['title']
            company_instance.location = company['location']
            company_instance.description = company['description']
            company_instance.employee_count = int(company['employee_count'])
            company_instance.save()

        for specialty in specialties:
            specialty_instance = Specialty()
            specialty_instance.code = specialty['code']
            specialty_instance.title = specialty['title']
            specialty_instance.save()

        for job in jobs:
            vacancy_instance = Vacancy()
            vacancy_instance.title = job['title']
            vacancy_instance.specialty = Specialty.objects.get(code=job['specialty'])
            vacancy_instance.company = Company.objects.get(pk=int(job['company']))
            vacancy_instance.skills = job['skills']
            vacancy_instance.description = job['description']
            vacancy_instance.salary_min = int(job['salary_from'])
            vacancy_instance.salary_max = int(job['salary_to'])
            date_list = job['posted'].split('-')
            date_instance = date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
            vacancy_instance.published_at = date_instance
            vacancy_instance.save()
