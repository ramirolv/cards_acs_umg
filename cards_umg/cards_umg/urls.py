from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('core', include('apps.core.urls')),
    #path('cards/', include('apps.cards.urls')),
]