from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import UserRegistrationSerializer, UserVerificationSerializer
from rest_framework.status import HTTP_200_OK, HTTP_304_NOT_MODIFIED, HTTP_404_NOT_FOUND
from .models import User
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .KYC import do_kyc
import re


# Create your views here.
@api_view(["POST"])
def usr_reg(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'user_registered': True}, status=HTTP_200_OK)
    return Response(serializer.errors)


@csrf_exempt
@api_view(["PUT"])
def usr_verification(request, pk):
    user = User.objects.get(pk=pk)
    print(user)
    serializer = UserVerificationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.update(user, serializer.validated_data)
        user_data = do_kyc(user)
        user.save()
        return Response(user_data, status=HTTP_200_OK)
    return Response(serializer.errors, status=HTTP_404_NOT_FOUND)