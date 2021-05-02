from django.urls import path
from rest_framework import routers

from journal import views

router = routers.DefaultRouter()
router.register(r'api/entries', views.JournalEntryViewSet, basename='entry')


urlpatterns = [
    path('entries/', views.ListJournalEntries.as_view(), name='journalentry-list'),
    path('entries/<int:pk>/', views.JournalEntryDetail.as_view(), name='journalentry-detail'),
    path('delete/<int:pk>/', views.DeleteJournalEntry.as_view(), name='journalentry-delete'),
    path('edit/<int:pk>/', views.UpdateJournalEntry.as_view(), name='journalentry-edit'),
    path('upload/', views.CreateJournalEntry.as_view()),
    path('mark_viewed/<int:pk>/', views.mark_journal_entry, name='mark-journal-entry'),
]

urlpatterns += router.urls
