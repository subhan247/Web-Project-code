from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=80)  # percentage 0-100

    def __str__(self):
        return self.name