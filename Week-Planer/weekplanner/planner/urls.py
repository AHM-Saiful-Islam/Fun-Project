from django.urls import path
from . import views

urlpatterns = [
    path('', views.week_planner, name='week_planner'),
    path('add/', views.add_task, name='add_task'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
]