from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.edit import DeleteView, UpdateView
from rest_framework.viewsets import ModelViewSet

from todos.models import TodoEntry
from todos.serializers import TodoEntrySerializer
from organizer.constants import FILTER_CONSTANTS
from organizer.mixins import AuthorsObjectsMixin


class ListTodoEntries(LoginRequiredMixin, ListView, AuthorsObjectsMixin):
    model = TodoEntry

    def get_queryset(self):
        entries_qs = super().get_queryset()
        filter = self.request.GET.get('filter')
        if filter in FILTER_CONSTANTS:
            qs_filters = FILTER_CONSTANTS[filter]
            entries_qs = entries_qs.filter(**qs_filters)
        return entries_qs


class DetailTodoEntry(LoginRequiredMixin, DetailView, AuthorsObjectsMixin):
    model = TodoEntry


class UpdateTodoEntry(LoginRequiredMixin, UpdateView, AuthorsObjectsMixin):
    model = TodoEntry
    fields = ('text',)


class DeleteTodoEntry(LoginRequiredMixin, DeleteView, AuthorsObjectsMixin):
    model = TodoEntry
    success_url = reverse_lazy('todoentry-list')


class CreateTodoEntry(LoginRequiredMixin, CreateView, AuthorsObjectsMixin):
    model = TodoEntry
    fields = ('text',)

    def form_valid(self, form):
        entry = form.save(commit=False)
        entry.author = self.request.user
        entry.save()
        return super().form_valid(form)


@login_required
def mark_todo_complete(request, pk):
    entry = TodoEntry.objects.filter(author=request.user, pk=pk).first()
    if not entry:
        raise Http404
    entry.done_dt = timezone.now()
    entry.save()
    return HttpResponseRedirect(reverse('todoentry-detail', args=[str(entry.id),]))


class TodoEntryViewSet(ModelViewSet, LoginRequiredMixin, AuthorsObjectsMixin):
    serializer_class = TodoEntrySerializer
    queryset = TodoEntry.objects.all()

    def perform_create(self, instance):
        instance.save(author_id=self.request.user.id)


