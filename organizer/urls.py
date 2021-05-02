from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view()),
    path('journal/', include('journal.urls')),
    path('todo/', include('todos.urls')),
    path('rest_auth/', include('rest_auth.urls'))
]
