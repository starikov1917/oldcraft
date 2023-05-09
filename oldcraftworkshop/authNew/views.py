from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from secrets import token_hex
from random import randint
from django.core.mail import send_mail
import json
from .models import Token
from django.contrib.auth.models import User
from django.contrib.auth import login, logout

# Create your views here.


class GetAccess(APIView):
    def post(self, request):
        token = token_hex(16)
        code = randint(100000, 999999)
        data = request.data
        print(data)
        send_mail(
            f"{code}",
            f"code: {code}",
            "starikov1917@gmail.com",
            [data['email']],
            fail_silently=False,
        )
        newToken = Token.objects.create(
            token = token,
            code = code,
            email = data['email'])
        newToken.save()
        return Response(status=200, data=token)

class ConfirmEmail(APIView):
    def post(self, request):
        token = request.data["token"]
        code = request.data["code"]
        email = request.data["email"]
        tokens = Token.objects.filter(token=token, code=code, email=email)

        if tokens:
            users = list(User.objects.filter(email=email))
            if users:
                login(self.request, users[0])
                print("done=================")
                return Response(status=200, data=email)
            else:
                newUser = User(email=email, username=email)
                newUser.save()
                login(self.request, newUser)
                print("done=================sdfsd")
                return Response(status=201, data="Asdasdasd")
        else:
            return Response(status=404, data=False)

class Logout(APIView):
    def get(self, request):
        logout(request)
        return Response(status=200)

