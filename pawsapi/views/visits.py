from rest_framework import viewsets, status, permissions, serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from pawsapi.models import Visit, VisitAction, Action


class VisitOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class VisitActionSerializer(serializers.ModelSerializer):
    action_type = serializers.CharField(source="action.type", read_only=True)

    class Meta:
        model = VisitAction
        fields = "__all__"


class VisitSerializer(serializers.ModelSerializer):
    actions = VisitActionSerializer(source="visitaction_set", many=True, read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    visit_type_name = serializers.CharField(
        source="visit_type.visit_type", read_only=True
    )
    visit_frequency_description = serializers.CharField(
        source="visit_frequency.description", read_only=True
    )
    pet_type_name = serializers.CharField(source="pet_type.pet_type", read_only=True)

    class Meta:
        model = Visit
        fields = [
            "id",
            "visit_start_date",
            "visit_end_date",
            "date",
            "visit_type",
            "visit_type_name",
            "visit_frequency",
            "visit_frequency_description",
            "pet_type",
            "pet_type_name",
            "user",
            "actions",
        ]


class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=["get"], url_path="my-visits")
    def my_visits(self, request):
        user = request.user
        visits = Visit.objects.filter(user=user)
        serializer = self.get_serializer(visits, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes = [IsAuthenticated, VisitOwnerPermission]
        return super().get_permissions()

    @action(detail=True, methods=["post"], url_path="actions/<int:action_id>")
    def add_action_to_visit(self, request, pk=None, action_id=None):
        visit = self.get_object()
        try:
            action = Action.objects.get(pk=action_id)
        except Action.DoesNotExist:
            return Response(
                {"error": f"Action with id {action_id} does not exist."},
                status=status.HTTP_404_NOT_FOUND,
            )

        visit_action = VisitAction.objects.create(visit=visit, action=action)
        serializer = VisitActionSerializer(visit_action)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'], url_path='actions/remove/<int:action_id>')
    def remove_action_from_visit(self, request, pk=None, action_id=None):
        visit = self.get_object()
        try:
            visit_action = VisitAction.objects.get(visit=visit, action=action_id)
            visit_action.delete()
            return Response({'detail': 'Action removed from visit.'}, status=status.HTTP_204_NO_CONTENT)
        except VisitAction.DoesNotExist:
            return Response({'detail': 'Action not found in visit.'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=["post"], url_path="create")
    def create_visit(self, request):
        visit_serializer = self.get_serializer(data=request.data)
        if visit_serializer.is_valid():
            visit = visit_serializer.save(user=request.user)
            action_ids = request.data.get("actions", [])
            for action_id in action_ids:
                visit_action_data = {
                    "visit": visit.id,
                    "action": action_id,
                }
                visit_action_serializer = VisitActionSerializer(data=visit_action_data)
                if visit_action_serializer.is_valid():
                    visit_action_serializer.save()
                else:
                    visit.delete()
                    return Response(
                        visit_action_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            return Response(visit_serializer.data, status=status.HTTP_201_CREATED)
        return Response(visit_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
