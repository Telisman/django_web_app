from django.contrib import admin
from .models import ClientsUsers, UserEducation, UserWorkExperience

admin.site.register(ClientsUsers)
admin.site.register(UserEducation)
admin.site.register(UserWorkExperience)
