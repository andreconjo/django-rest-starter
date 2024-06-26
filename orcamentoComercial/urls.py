# meu_projeto/orcamentoComercial/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrcamentoComercialViewSet
from .views import login
from .views import get_csrf_token




router = DefaultRouter()
router.register(r'orcamento', OrcamentoComercialViewSet)  

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login, name='login'),
    path('csrf/', get_csrf_token, name='csrf_token'),

]
