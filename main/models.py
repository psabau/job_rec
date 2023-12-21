from django.db import models
from django.contrib.auth.models import User

class Applicant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    posted_on = models.DateField(auto_now_add=True)
    last_date_to_apply = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    applied_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('APPLIED', 'Applied'), ('REJECTED', 'Rejected'), ('ACCEPTED', 'Accepted')])

    def __str__(self):
        return f"{self.applicant.user.username} - {self.job.title}"

from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username