from rest_framework import serializers
from fintech.models import Transacao, Categoria

class TransacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacao
        fields = '__all__'

    def validate_valor(self, value):
        if value <= 0:
            raise serializers.ValidationError('O valor de uma transacao deve ser maior que 0!')
        return value

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
