from django.contrib import admin

from userapp.models import UserProfile, Project,Experience,Certification,Qualifications

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(Certification)
admin.site.register(Qualifications)



