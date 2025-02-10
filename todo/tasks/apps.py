from django.apps import AppConfig

class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todo.tasks'  # Burada 'tasks' yerine 'todo.tasks' olmalı!
