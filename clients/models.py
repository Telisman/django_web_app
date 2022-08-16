from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class ClientsUsers(AbstractUser):
    worker = '1'
    owner = '2'
    USER_TYPE_CHOICE = (
        (worker, 'Worker'),
        (owner, 'Owner')
    )
    user_type = models.CharField(max_length=100, blank=True, choices=USER_TYPE_CHOICE)
    username = models.CharField(max_length=100, unique=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    profile_image = models.ImageField(null=True, blank=True, default=None)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    email = models.EmailField(max_length=300,validators=[RegexValidator(regex="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.["r"a-zA-Z0-9-.]+$",
                                                                        message='please enter the correct format')])
    date_of_birth = models.DateField(null=True)
    bio = models.TextField(default=" ")
    # date_of_birth = models.DateField(default=None)

    def __str__(self):
        return self.username + ' | ' +self.last_name + ' | ' + self.first_name + ' | ' + str(self.phone_number) + ' | ' + self.user_type + ' | ' + self.email+ ' | ' + str(self.id)