from rest_framework.permissions import IsAuthenticated

from habits.models import Habits
from rest_framework import viewsets, generics

from habits.paginators import HabitsPaginator
from habits.serializers import HabitsSerializer
from users.permissions import IsOwner


class HabitsView(viewsets.ModelViewSet):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    pagination_class = HabitsPaginator

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action == ("create", "list"):
            self.permission_classes = (IsAuthenticated,)
        if self.action in ("destroy", "update", "partial_update"):
            self.permission_classes = (IsAuthenticated, IsOwner)

        return super().get_permissions()

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class HabitsPublicListAPIView(generics.ListAPIView):
    queryset = Habits.objects.filter(is_public=True)
    serializer_class = HabitsSerializer
    pagination_class = HabitsPaginator

    # def get_queryset(self):
    #     if self.action == "list" and self.request.user.is_authenticated:
    #         return self.queryset.filter(owner=self.request.user)
