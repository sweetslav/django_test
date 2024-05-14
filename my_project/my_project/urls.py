from django.contrib import admin
from django.urls import path, include
from myapp3.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prefix/', include('myapp.urls')),
    path('les3/', include('myapp3.urls')),
    path('les4/', include('myapp4.urls')),
    path('les6/', include('myapp6.urls')),
    # path('__debug__', include('debug_toolbar.urls')),
    path('', index),
]
