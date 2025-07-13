from rest_framework import serializers

from .models import Eleccion, Votante, Partido, Candidato, VotanteEleccion, Voto

class EleccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eleccion
        fields = '__all__' 

class VotanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Votante
        fields = '__all__'

class PartidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partido
        fields = '__all__'

class CandidatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidato
        fields = '__all__'

class VotanteEleccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VotanteEleccion
        fields = '__all__'

class VotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voto
        fields = '__all__'

class VotoCandidatoSerializer(serializers.Serializer):
    candidato = serializers.CharField(max_length=100)
    votos = serializers.IntegerField()