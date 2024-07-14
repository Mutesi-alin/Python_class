from django.urls import path

from .views import studentListView

urlpatterns = [
    path('students/', studentListView.as_view(),name="student_list_view"),

]


