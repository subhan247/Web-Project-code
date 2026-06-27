from django.shortcuts import render
from .models import Bio
from education.models import Education
from skills.models import Skill
from experience.models import Experience

def home(request):
    bio = Bio.objects.first()
    educations = Education.objects.all()
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    return render(request, 'portfolio/home.html', {
        'bio': bio,
        'educations': educations,
        'skills': skills,
        'experiences': experiences,
    })