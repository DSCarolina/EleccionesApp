from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Eleccion, Votante, Partido, Candidato, VotanteEleccion, Voto
from .serializers import EleccionSerializer, VotanteSerializer, PartidoSerializer, CandidatoSerializer, VotoSerializer,VotoCandidatoSerializer,VotanteEleccionSerializer
from django.db.models import  Count
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view

def index(request):
    return HttpResponse("Sistema de registro para Elecciones Presidenciales")   
# Create your views here.

class EleccionViewSet(viewsets.ModelViewSet):
    queryset = Eleccion.objects.all()
    serializer_class = EleccionSerializer

class VotanteViewSet(viewsets.ModelViewSet):
    queryset = Votante.objects.all()
    serializer_class = VotanteSerializer

class VotanteEleccionViewSet(viewsets.ModelViewSet):
    queryset = VotanteEleccion.objects.all()
    serializer_class = VotanteEleccionSerializer

class PartidoCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Partido.objects.all()
    serializer_class = PartidoSerializer

class VotoCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Voto.objects.all()
    serializer_class = VotoSerializer

class CandidatoCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializer

@api_view(['GET'])
def votos_count(request):
    try:
        cantidadblanco = Voto.objects.filter(candidato__isnull=True).count()
        cantidadValido = Voto.objects.filter(candidato__isnull=False).count()
        return JsonResponse({'cantidad_blanco': cantidadblanco,'cantidad_valido': cantidadValido}, safe=False, status=200)
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)

#Votos blancos y válidos
@api_view(['GET'])
def votos_count(request):
    try:
        cantidadblanco = Voto.objects.filter(candidato__isnull=True).count()
        cantidadValido = Voto.objects.filter(candidato__isnull=False).count()
        return JsonResponse({'cantidad_blanco': cantidadblanco,'cantidad_valido': cantidadValido}, safe=False, status=200)
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)

#Votos por candidatos

@api_view(['GET'])
def votos_candidatos_count(request): 
    try:
        votos_candidato = Voto.objects.filter(
            candidato__isnull=False
        ).values(
            'candidato__nombre__nombre',
            'candidato__nombre__apellido'
        ).annotate(
            total_votos=Count('id')
        )

        resultado = []
        for item in votos_candidato:
            resultado.append({
                'candidato': f"{item['candidato__nombre__nombre']} {item['candidato__nombre__apellido']}",
                'votos': item['total_votos']
            })
        return JsonResponse(VotoCandidatoSerializer(resultado, many=True).data, safe=False, status=200)

    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)
