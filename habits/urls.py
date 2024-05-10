from django.urls import path
from rest_framework import routers

from habits.apps import HabitsConfig
from habits.views import HabitsView, HabitsPublicListAPIView

name = HabitsConfig.name


router = routers.DefaultRouter()
router.register(r"habits", HabitsView, basename="habits")

urlpatterns = [
    path("public_habits/", HabitsPublicListAPIView.as_view(), name="public_habits"),

] + router.urls
