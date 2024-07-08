from rest_framework import viewsets  
from .models import OrcamentoComercial, Cargo, Senioridade, Pagamento, Area
from .serializers import OrcamentoComercialSerializer, CargoSerializer, PagamentoSerializer, UserSerializer, AreaSerializer, SenioridadeSerializer
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import authenticate, login
import json
from django.middleware.csrf import get_token
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.middleware.csrf import get_token
from django.http import JsonResponse
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

class OrcamentoComercialViewSet(viewsets.ModelViewSet):
    queryset = OrcamentoComercial.objects.all()
    serializer_class = OrcamentoComercialSerializer

class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

class SenioridadeViewSet(viewsets.ModelViewSet):
    queryset = Senioridade.objects.all()
    serializer_class = SenioridadeSerializer

class PagamentoViewSet(viewsets.ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer

class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class UserDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)
