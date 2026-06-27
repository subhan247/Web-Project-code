from django.db import models

class Bio(models.Model):
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile/', blank=True)
    hero_text = models.TextField(help_text="Short text shown on home section")
    description = models.TextField(help_text="Full bio shown in Bio section")
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name