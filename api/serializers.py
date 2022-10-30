from rest_framework import serializers
from api.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    # contactNo = serializers.DecimalField(decimal_places=0, max_digits=10, read_only=True)
    # imgFront = serializers.ImageField()
    # imgBack = serializers.ImageField()

    class Meta:
        model = User
        fields = ['contactNo', 'firstName', 'middleName', 'lastName', 'dob', 'gender', 'houseNo', 'streetName',
                  'localityName', 'cityName', 'countryName', 'pinCode']#, 'idImageFront', 'idImageBack']


class UserVerificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['idImageFront', 'idImageBack', 'userPhoto']

