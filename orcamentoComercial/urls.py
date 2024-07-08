# orcamentoComercial/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import OrcamentoComercialViewSet, UserDetailView, CargoViewSet, SenioridadeViewSet, PagamentoViewSet, AreaViewSet

router = DefaultRouter()
router.register(r'orcamento', OrcamentoComercialViewSet)  
router.register(r'cargos', CargoViewSet)
router.register(r'senioridade', SenioridadeViewSet)
router.register(r'pagamento', PagamentoViewSet)
router.register(r'area', AreaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', UserDetailView.as_view(), name='user_detail'),
]
