from rest_framework.generics import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import Group
from .models import CustomUser
from .serializers import UserSerializer, GroupSerializer

from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions


from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm


###

from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)


###


class UserView(ListCreateAPIView):

    model=get_user_model()


    permission_classes = [
                          permissions.AllowAny
                          ]

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class SingleUserView(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class MyUserDataView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user


class GroupView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = GroupSerializer

class SingleGroupView(RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
