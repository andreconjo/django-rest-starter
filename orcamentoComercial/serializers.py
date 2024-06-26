from rest_framework import serializers
from orcamentoComercial.models import OrcamentoComercial

class OrcamentoComercialSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrcamentoComercial
        fields = '__all__'

