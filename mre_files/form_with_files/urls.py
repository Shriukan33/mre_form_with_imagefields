from django.urls import path

from . import views

app_name = 'form_with_files'

urlpatterns = [
    path('new/', views.MyView.as_view(), name='new'),
    path('edit/<int:pkid>/', views.MyView.as_view(), name='edit'),
]