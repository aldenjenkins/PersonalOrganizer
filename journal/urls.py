from django.urls import path

from journal import views


urlpatterns = [
    path('entries/', views.ListJournalEntries.as_view(), name='journalentry-list'),
    path('entries/<int:pk>/', views.JournalEntryDetail.as_view(), name='journalentry-detail'),
    path('delete/<int:pk>/', views.DeleteJournalEntry.as_view(), name='journalentry-delete'),
    path('edit/<int:pk>/', views.UpdateJournalEntry.as_view(), name='journalentry-edit'),
    path('upload/', views.CreateJournalEntry.as_view()),
    path('mark_viewed/<int:pk>/', views.mark_journal_entry, name='mark-journal-entry'),
]
