from django.urls import path

from todos import views


urlpatterns = [
    path('entries/', views.ListTodoEntries.as_view(), name='todoentry-list'),
    path('entries/<int:pk>/', views.DetailTodoEntry.as_view(), name='todoentry-detail'),
    path('delete/<int:pk>/', views.DeleteTodoEntry.as_view(), name='todoentry-delete'),
    path('edit/<int:pk>/', views.UpdateTodoEntry.as_view(), name='todoentry-update'),
    path('upload/', views.CreateTodoEntry.as_view(), name='todoentry-create'),
    path('complete/<int:pk>/', views.mark_todo_complete, name='todoentry-complete'),
]
