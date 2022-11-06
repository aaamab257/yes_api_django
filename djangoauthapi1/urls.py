from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/material/', include('material.urls')),
    path('api/user/', include('account.urls'))
]
