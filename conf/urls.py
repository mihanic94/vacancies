from django.contrib import admin
from django.urls import path, include

from vacancies.views import page_not_found, server_error

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vacancies.urls')),
]

handler404 = page_not_found
handler500 = server_error
