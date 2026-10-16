


from django.urls import path
from .views import Index, Equipe, Modalidade

urlpatterns = [
    path('',Index, name="index"),
    path('/equipe',Equipe, name="equipe"),
    path('/modalidade',Modalidade, name="modalidade")
]