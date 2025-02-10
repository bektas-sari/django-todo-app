from django.urls import path
from .views import task_list, task_complete, task_delete

urlpatterns = [
    path('', task_list, name='task_list'),
    path('complete/<int:task_id>/', task_complete, name='task_complete'),  # Tamamlama URL'si
    path('delete/<int:task_id>/', task_delete, name='task_delete'),  # Silme URL'si
]
