from django.shortcuts import render

# Create your views here.


from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import *
from rest_framework import viewsets



@api_view()
def livro1(request):
    livro = Livro.objects.get(id=3)
    contexto = {
        "Nome do Livro": livro.nome
    }
    return Response(contexto)

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
