from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.response import Response
from pawsapi.models import VisitFrequency


class VisitFrequencySerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitFrequency
        fields = "__all__"


class VisitFrequencyViewSet(viewsets.ViewSet):
    def list(self, request):
        visit_frequencies = VisitFrequency.objects.all()
        serializer = VisitFrequencySerializer(visit_frequencies, many=True)
        return Response(serializer.data)
