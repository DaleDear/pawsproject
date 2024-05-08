from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.response import Response
from pawsapi.models import Action


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = "__all__"


class ActionViewSet(viewsets.ViewSet):
    def list(self, request):
        actions = Action.objects.all()
        serializer = ActionSerializer(actions, many=True)
        return Response(serializer.data)
