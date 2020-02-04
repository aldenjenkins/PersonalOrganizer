from rest_framework.serializers import ModelSerializer

from journal.models import JournalEntry

class JournalEntrySerializer(ModelSerializer):
    class Meta:
        model = JournalEntry
