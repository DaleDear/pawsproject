from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.response import Response
from pawsapi.models import PetType


class PetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetType
        fields = "__all__"


class PetTypeViewSet(viewsets.ViewSet):
    def list(self, request):
        pet_types = PetType.objects.all()
        serializer = PetTypeSerializer(pet_types, many=True)
        return Response(serializer.data)
