from django.contrib import admin

from vacancies.models import Company, Specialty, Vacancy

admin.site.register(Company)
admin.site.register(Specialty)
admin.site.register(Vacancy)
