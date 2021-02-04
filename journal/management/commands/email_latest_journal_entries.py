import markdown

from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.shortcuts import reverse

from journal.models import JournalEntry


class Command(BaseCommand):
    help = "Generate email for unread journal entries."

    def handle(self, *args, **options):
        print(f'email sending started at UTC {datetime.now().strftime("%Y-%m-%d")}')
        user = User.objects.first()
        unread_journal_entries = JournalEntry.objects.filter(
            author=user, read_dt__isnull=True
        )
        journals_combined = ' \n \n--- \n \n'.join(
            [
                "#" + str(entry.created.strftime("%Y-%m-%d")) + '\n\n' + entry.text
                for entry in unread_journal_entries
            ]
        )
        entry_text = (
            'Unread journal entries: \n \n'
            + f'{journals_combined}'
            + ' \n--- \n \n'
            + 'Click here to set each entry as read individually: \n'
            + f'http://{settings.ALLOWED_HOSTS[1] + reverse("journalentry-list")}'
        )
        html_entry = markdown.markdown(entry_text)
        send_mail(
            subject=f'{timezone.now().strftime("%Y-%m-%d")} Unread Journal Entries',
            message=entry_text,
            from_email="organizerbot@aldenjenkins.com",
            recipient_list=settings.EMAIL_TO,
            html_message=html_entry,
        )
        print(f'email sending done at UTC {datetime.now().strftime("%Y-%m-%d")}')
