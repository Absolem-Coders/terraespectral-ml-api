# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('ai/', AiListView.as_view(), name='ai-list'),
     path('ores/', AiModelView.as_view(), name='ai-list'),
]
