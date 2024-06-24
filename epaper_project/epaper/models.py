# epaper/models.py

from django.db import models

class ScrapedData(models.Model):
    json_data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
