from django.db import models

class Experience(models.Model):
    TYPE_CHOICES = [
        ('academic', 'Academic'),
        ('professional', 'Professional'),
        ('project', 'Project'),
    ]
    title = models.CharField(max_length=150)
    organization = models.CharField(max_length=150)
    exp_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='project')
    year_start = models.IntegerField()
    year_end = models.IntegerField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title