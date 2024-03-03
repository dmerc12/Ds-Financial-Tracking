from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('entry.urls')),
    path('financial/tracker/', include('finance_tracking.urls')),
    path('users/', include('users.urls')),
]
