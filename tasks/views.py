from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import AnonymousUser
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwner


class TaskViewSet(ModelViewSet):

    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    filterset_fields = ["completed"]

    # IMPORTANT: add dummy queryset for swagger
    queryset = Task.objects.none()

    def get_queryset(self):
        # Swagger fix
        if getattr(self, "swagger_fake_view", False):
            return Task.objects.none()

        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)