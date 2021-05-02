from rest_framework.serializers import ModelSerializer

from journal.models import JournalEntry

class JournalEntrySerializer(ModelSerializer):
    class Meta:
        model = JournalEntry
        fields = ('id', 'created', 'text', 'author', 'read_dt')
        read_only_fields =  ('id', 'author')
