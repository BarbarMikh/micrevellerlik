from django.db import models

class SiteStats(models.Model):
    visitors = models.PositiveIntegerField(default=0)
    emails_sent = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Visitors: {self.visitors}, Emails Sent: {self.emails_sent}"
