from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from django_extensions.db.models import TimeStampedModel


class JournalEntryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset.select_related('author')


class JournalEntry(TimeStampedModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='journal_entries', null=False, blank=False)
    email_sent_dt = models.DateTimeField(null=True, blank=True)
    text = models.TextField(null=False, blank=False)
    read_dt = models.DateTimeField(null=True, blank=True)
    objects = JournalEntryManager

    class Meta:
        verbose_name_plural = "Journal Entries"
        verbose_name = "Journal Entry"

    def __str__(self):
        return f'{self.created.date()} {self.author.username}'

    def __repr__(self):
        return self.__str__()

    def get_absolute_url(self):
        return reverse('journalentry-detail', args=[str(self.id)])

    @property
    def was_read(self):
        return self.read_dt is not None
