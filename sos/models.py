from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator, MinLengthValidator


class User(AbstractUser):
    GENDER = (
        (1, 'Male'),
        (2, 'Female'),
        (3, 'Transgender'),
    )

    mobile = models.CharField(
        max_length=10,
        unique=True,
        null=False,
    )
    isMobileVerified = models.BooleanField(default=True)
    dob = models.DateField(auto_now=False, auto_now_add=False,null=True, blank=True)
    gender = models.IntegerField(choices=GENDER, blank=True, null=True)
    blood_group = models.CharField(blank=True, null=True, max_length=10)

    latitude = models.DecimalField(max_digits=16, decimal_places=14, blank=True, null=True)
    longitude = models.DecimalField(max_digits=16, decimal_places=14, blank=True, null=True)

    gcm = models.CharField(max_length=200, null=True, blank=True)


    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

