from rest_framework import serializers
from api.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['contactNo', 'firstName', 'middleName', 'lastName', 'dob', 'gender', 'houseNo', 'streetName',
                  'localityName', 'cityName', 'countryName', 'pinCode']


class UserVerificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['idImageFront', 'idImageBack', 'userPhoto']

