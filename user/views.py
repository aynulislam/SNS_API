from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework.exceptions import NotAcceptable
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, \
    MyTokenObtainPairSerializer, UserInfoSerializer, UserLoginHistorySerialize
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import ScUser, ScLoginHistory
from django.db import transaction
from django.db import connection
from django.core.mail import send_mail, EmailMessage
from django.conf import settings


class UserCreate(APIView):
    @staticmethod
    def send_email(content):
        subject = 'Thank you for registering to our site'
        html_content = render_to_string('mail.html', {'content': content})
        print(html_content)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [content['mail'], 'rhmithu50@gmail.com']
        msg = EmailMessage(subject=subject, body=html_content, from_email=email_from, bcc=recipient_list)
        msg.content_subtype = "html"
        return msg.send()

    permission_classes = [AllowAny]
    @transaction.atomic
    def post(self, request):
        data = request.data
        new_user = {"username": data["email"], "email": data["email"], "password": data["password"]}
        serializer = UserSerializer(data=new_user)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                data_info = {"user_name": data["user_name"], "user": user.id}
                cursor = connection.cursor()
                ch = data_info['user_name'][0]
                cursor.execute("select max(right(user_code,5)) from user_scuser where left(user_name,1)=%s", ch)
                row = cursor.fetchone()
                print(type(row[0]))
                if type(row[0]) == str and row[0] != '':
                    print("ami to thik: ", row)
                    row = int(row[0]) + 1
                    print("Etto problem kn??: ", row)
                else:
                    row = 10000
                print("The row is: ",row)
                row = str(row)
                row = 'W' + ch + row
                data_info["user_code"] = row
                print(user.id)
                serializer_info = UserInfoSerializer(data=data_info, partial=True)
                if serializer_info.is_valid():
                    print("Yes i am here")
                    serializer_info.save()
                    self.send_email({"name": data["user_name"], 'code': data_info["user_code"], 'mail': data["email"]})
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    raise NotAcceptable('Save Error')

        else:
            raise NotAcceptable('Save Error')


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, pk):
        print("Hello")
        user = get_object_or_404(ScUser, pk=pk)
        serializer = UserInfoSerializer(user)
        return Response(serializer.data)

    def post(self, request, pk):
        data = request.data
        cursor = connection.cursor()
        ch = data['user_name'][0]
        cursor.execute("select max(right(user_code,5)) from user_scuser where left(user_name,1)=%s", ch)
        row = cursor.fetchone()
        if type(row[0]) == str:
            row = int(row[0])+1
        else:
            row = 10000
        row = str(row)
        row = 'W'+ch+row
        print("Max_Hasan", row)
        data["user_code"]=row
        serializer = UserInfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            content = {
                'status': 'request was not permitted'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    def patch(self, request, pk):
        data = request.data
        serializer = UserInfoSerializer(data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "Success"}, status=status.HTTP_201_CREATED)
        return Response({"response": "Failed"}, status=status.HTTP_400_BAD_REQUEST)


class UserLoginInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        info = ScLoginHistory.objects.all().filter(user=request.user)
        serializer = UserLoginHistorySerialize(info, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        ip = request.META.get('REMOTE_ADDR')
        data["ip"] = ip
        data["user"] = request.user.id
        serializer = UserLoginHistorySerialize(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "Success"}, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            content = {
                'status': 'request was not permitted'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
