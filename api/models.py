from django.db import models


# Create your models here.
class User(models.Model):
    contactNo = models.BigIntegerField(primary_key=True)
    firstName = models.CharField(max_length=50, blank=False)
    middleName = models.CharField(max_length=50, blank=True)
    lastName = models.CharField(max_length=50, blank=True)
    dob = models.DateField()
    gender = models.CharField(max_length=6)
    houseNo = models.CharField(max_length=10)
    streetName = models.CharField(max_length=50)
    localityName = models.CharField(max_length=50)
    cityName = models.CharField(max_length=20)
    countryName = models.CharField(max_length=20)
    pinCode = models.IntegerField()
    kycVerified = models.BooleanField(default=False)
    idImageFront = models.ImageField(upload_to='UserID_front')
    idImageBack = models.ImageField(upload_to='UserID_back')
    userPhoto = models.ImageField(upload_to='UserPhoto')
