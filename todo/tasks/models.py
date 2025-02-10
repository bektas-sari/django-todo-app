from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)  # Görev başlığı
    completed = models.BooleanField(default=False)  # Görev tamamlandı mı?
    created_at = models.DateTimeField(auto_now_add=True)  # Oluşturulma tarihi

    def __str__(self):
        return self.title  # Admin panelinde gösterimi kolaylaştırır

