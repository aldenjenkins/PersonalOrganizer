from django.contrib.auth.models import User

from journal.models import JournalEntry


def get_latest_journal_entry(user):
    return