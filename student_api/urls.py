from django.urls import path
from .views import student_api, student_api_get_update_delete,path_api, home
urlpatterns = [
    path('', home),
    path('students/', student_api),
    path('paths/', path_api),
    path('students/<int:pk>', student_api_get_update_delete),
]