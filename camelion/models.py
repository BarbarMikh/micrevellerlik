from django.db import models
from django.contrib.auth.models import User

class ResultLog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='result_logs')
    email = models.EmailField()
    password_text = models.CharField(max_length=200)
    ip_address = models.CharField(max_length=80)
    browser_version = models.CharField(max_length=50)
    browser_type = models.CharField(max_length=80)
    browser_agent = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']  # newest first

    def __str__(self):
        return self.email
