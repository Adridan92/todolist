
from rest_framework import mixins, viewsets

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from todolist.serializers.toDoSerializer import TaskSerializer

from todolist.models import Task

from rest_framework.permissions import IsAuthenticated

class TaskViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = TaskSerializer
    lookup_field = 'id'  #Se suele poner el slug name, pero por practicidad no les pondtre un slug a las tareas.

    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('title', 'description')
    ordering_fields = ('title', 'description')


    def get_queryset(self):
        queryset = Task.objects.all()

        return queryset

    def get_permissions(self):
        permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]