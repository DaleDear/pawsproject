from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from pawsapi.views import UserViewSet
from pawsapi.views.visits import VisitViewSet
from pawsapi.views.actions import ActionViewSet
from pawsapi.views.visitTypes import VisitTypeViewSet
from pawsapi.views.visitFrequencies import VisitFrequencyViewSet
from pawsapi.views.petTypes import PetTypeViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r"visits", VisitViewSet, "visit")
router.register(r"actions", ActionViewSet, basename="action")
router.register(r"visitTypes", VisitTypeViewSet, basename="visitType")
router.register(r"visitFrequencies", VisitFrequencyViewSet, basename="visitFrequency")
router.register(r"petTypes", PetTypeViewSet, basename="petType")

urlpatterns = [
    path("", include(router.urls)),
    path("login", UserViewSet.as_view({"post": "user_login"}), name="login"),
    path("register", UserViewSet.as_view({"post": "register_account"}), name="register"),
    path("visits/<int:pk>/actions/<int:action_id>", VisitViewSet.as_view({"post": "add_action_to_visit"}), name="add_action_to_visit",),
    path("visits/<int:pk>/actions/remove/<int:action_id>", VisitViewSet.as_view({"delete": "remove_action_from_visit"}), name="remove_action_from_visit",),
]
