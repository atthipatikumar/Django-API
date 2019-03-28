from rest_framework import serializers
from myapp.models import Task
from rest_framework import viewsets

class NoteSerialiser(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'created_at', 'created_by', 'priority')


class NoteViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = NoteSerialiser