from rest_framework import serializers
from orcamentoComercial.models import OrcamentoComercial, Cargo, Senioridade, Pagamento, Area
from django.contrib.auth.models import User

class OrcamentoComercialSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrcamentoComercial
        fields = '__all__'

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'

class SenioridadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Senioridade
        fields = '__all__'

class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = '__all__'

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']