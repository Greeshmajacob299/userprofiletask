from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    postcode = models.IntegerField(null=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    qualification = models.CharField(max_length=200)
    skill1 = models.CharField(max_length=255)
    skill2 = models.CharField(max_length=255)
    skill3 = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.user.username)

class Project(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    projectname = models.CharField(max_length=255)
    description = models.TextField()
    projectimage = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return '{}'.format(self.projectname)

class Experience(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    companyname = models.CharField(max_length=255)
    jobrole = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    responsibility = models.TextField()

    def __str__(self):
        return '{}'.format(self.companyname)

class Qualifications(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=255)
    yearofpassing = models.CharField(max_length=200)
    percentage = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.qualification)

class Certification(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    certificatename = models.CharField(max_length=255)
    certificateimage = models.ImageField(upload_to='certificate_images/')

    def __str__(self):
        return '{}'.format(self.certificatename)
