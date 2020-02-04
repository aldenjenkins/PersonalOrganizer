import datetime
import markdown

from django import template as t
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import Http404, HttpResponseRedirect
from django.template import Template, Context
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import DeleteView, UpdateView

from journal.forms import JournalEditForm
from journal.models import JournalEntry
from organizer.constants import FILTER_CONSTANTS
from organizer.mixins import AuthorsObjectsMixin


class ListJournalEntries(LoginRequiredMixin, ListView, AuthorsObjectsMixin):
    model = JournalEntry

    def get_queryset(self):
        entries_qs = super().get_queryset()
        filter = self.request.GET.get('filter', None)
        if filter in FILTER_CONSTANTS:
            kwargs = FILTER_CONSTANTS[filter]
            entries_qs = entries_qs.filter(**kwargs)
        return entries_qs


class CreateJournalEntry(LoginRequiredMixin, CreateView):
    model = JournalEntry
    fields = ('text',)

    def form_valid(self, form):
        entry = form.save(commit=False)
        entry.author = self.request.user
        entry.save()
        return super(CreateJournalEntry, self).form_valid(form)


class DeleteJournalEntry(LoginRequiredMixin, DeleteView, AuthorsObjectsMixin):
    model = JournalEntry
    success_url = reverse_lazy('journalentry-list')


class UpdateJournalEntry(LoginRequiredMixin, UpdateView, AuthorsObjectsMixin):
    model = JournalEntry
    fields = ('text',)


class JournalEntryDetail(LoginRequiredMixin, DetailView, AuthorsObjectsMixin):
    model = JournalEntry

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        journal_text_html = markdown.markdown(kwargs['object'].text)
        data['md_formatted_journal_text'] = journal_text_html
        return data


def mark_journal_entry(request, pk):
    entry = JournalEntry.objects.filter(author=request.user, pk=pk).first()
    if not entry:
        raise Http404
    entry.read_dt = timezone.now()
    entry.save()
    return HttpResponseRedirect(reverse('journalentry-detail', args=[str(pk),]))

