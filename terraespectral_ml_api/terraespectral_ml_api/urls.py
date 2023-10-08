# urls.py no seu projeto principal
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('mlapi.urls')),  # 'seu_app' é o nome do seu aplicativo
]
