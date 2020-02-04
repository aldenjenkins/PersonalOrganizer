from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

from django_extensions.db.models import TimeStampedModel


class TodoEntry(TimeStampedModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todo_entries', null=False, blank=False)
    email_sent_dt = models.DateTimeField(null=True, blank=True)
    done_dt = models.DateTimeField(null=True, blank=True)
    text = models.TextField(null=False, blank=False)

    class Meta:
        verbose_name = "Todo Entry"
        verbose_name_plural = "Todo Entries"

    def __str__(self):
        return f'{self.created.date()} - {self.text}'

    def __repr__(self):
        return f'{self.id} {self.__str__()}'

    @property
    def is_done(self):
        return self.done_dt is not None

    def get_absolute_url(self):
        return reverse('todoentry-detail', args=[str(self.id)])


