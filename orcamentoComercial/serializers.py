from rest_framework import serializers
from orcamentoComercial.models import OrcamentoComercial, Cargo
from django.contrib.auth.models import User

class OrcamentoComercialSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrcamentoComercial
        fields = '__all__'

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']