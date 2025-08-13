from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('gest_store.urls')),  # Inclure les URLs de l'API
]