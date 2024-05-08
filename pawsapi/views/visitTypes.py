from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.response import Response
from pawsapi.models import VisitType


class VisitTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitType
        fields = "__all__"


class VisitTypeViewSet(viewsets.ViewSet):
    def list(self, request):
        visit_types = VisitType.objects.all()
        serializer = VisitTypeSerializer(visit_types, many=True)
        return Response(serializer.data)
