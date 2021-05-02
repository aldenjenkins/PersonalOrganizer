from rest_framework.serializers import ModelSerializer

from todos.models import TodoEntry

class TodoEntrySerializer(ModelSerializer):
    class Meta:
        model = TodoEntry
        fields = ('id', 'text', 'done_dt')
