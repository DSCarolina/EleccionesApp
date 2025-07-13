from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'elecciones', views.EleccionViewSet)
router.register(r'votantes', views.VotanteViewSet)
router.register(r'votanteselecciones', views.VotanteEleccionViewSet)


urlpatterns = [
    # path('', views.index, name='index'),
    path('',include(router.urls)),
    path('partidos/', views.PartidoCreateView.as_view(), name='partido-create-list'),
    path('votos/', views.VotoCreateView.as_view(), name='voto-create-list'),
    path('votos/cantidad/', views.votos_count, name='votos-count'),
    path('votos/cantidad_votos_candidatos/', views.votos_candidatos_count, name='votos-candidatos-count'),
    path('candidatos/', views.CandidatoCreateView.as_view(), name='candidato-create-list'),

]