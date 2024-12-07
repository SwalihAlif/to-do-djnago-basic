from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('complete/<int:task_id>/', views.mark_complete, name='mark_complete'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task')
]