from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from journal.models import JournalEntry
from digest.utils import construct_digest_email_text
from todos.models import TodoEntry

class Command(BaseCommand):
    help = 'Sends a daily digest to each user that includes the unread journal entries and unfinished todos. Should be read when waking up.'

    def handle(self, *args, **options):
        for user in User.objects.all():
            todos = TodoEntry.objects.filter(done_dt=None, author=user)
            journals = JournalEntry.objects.filter(read_dt=None, author=user)
            email_text = construct_digest_email_text(todos, journals)
            send_mail(
                f'Organizer Digest {timezone.now().date()}',
                email_text,
                'alden@aldenjenkins.com',
                ['alden@aldenjenkins.com',],
            )
        self.stdout.write(self.style.SUCCESS('Successfully sent digest mail.'))
