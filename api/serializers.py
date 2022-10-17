from rest_framework import serializers
from api.models import *


class LivroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Livro
        fields = ['nome', 'autor', 'categoria', 'descricao']
