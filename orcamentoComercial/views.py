from rest_framework import viewsets  
from .models import OrcamentoComercial  
from .serializers import OrcamentoComercialSerializer 
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
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.middleware.csrf import get_token
from django.http import JsonResponse


class OrcamentoComercialViewSet(viewsets.ModelViewSet):
    queryset = OrcamentoComercial.objects.all()
    serializer_class = OrcamentoComercialSerializer


User = get_user_model()

def create_jwt_pair_for_user(user: User):
    access = AccessToken.for_user(user)
    refresh = RefreshToken.for_user(user)
    access_payload = access.payload
    access_payload['name'] = user.get_full_name()
    access_payload['username'] = user.username
    access_payload['permissions'] = list(user.get_all_permissions())
    groups = user.groups.values_list('name', flat=True)
    access_payload['groups'] = list(groups)
    tokens = {"access": str(access), "refresh": str(refresh)}
    return tokens

@api_view(['POST'])
def login(request):
    try:
        username = request.data.get('username')
        password = request.data.get('password')
        usuario = User.objects.get(username=username)

        if usuario is not None and check_password(password, usuario.password):
            tokens = create_jwt_pair_for_user(usuario)
            response = {"message": "Login Successful", "tokens": tokens}
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)




def get_csrf_token(request):
    token = get_token(request)
    return JsonResponse({'csrfToken': token})
