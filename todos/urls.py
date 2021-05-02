from django.urls import path
from rest_framework import routers

from todos import views

router = routers.DefaultRouter()
router.register(r'api/entries', views.TodoEntryViewSet, basename='entry')

urlpatterns = [
    path('entries/', views.ListTodoEntries.as_view(), name='todoentry-list'),
    path('entries/<int:pk>/', views.DetailTodoEntry.as_view(), name='todoentry-detail'),
    path('delete/<int:pk>/', views.DeleteTodoEntry.as_view(), name='todoentry-delete'),
    path('edit/<int:pk>/', views.UpdateTodoEntry.as_view(), name='todoentry-update'),
    path('upload/', views.CreateTodoEntry.as_view(), name='todoentry-create'),
    path('complete/<int:pk>/', views.mark_todo_complete, name='todoentry-complete'),
]

urlpatterns += router.urls
