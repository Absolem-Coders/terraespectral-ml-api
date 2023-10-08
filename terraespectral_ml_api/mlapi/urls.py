# urls.py
from django.urls import path
from .views import AiListView

urlpatterns = [
    path('ai/', AiListView.as_view(), name='ai-list'),
]
