
from rest_framework import serializers

from todolist.models import Status, Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id','title','description', 'status')



