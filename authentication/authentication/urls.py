
from django.contrib import admin
from django.urls import path,include
from authapp import urls
import authapp



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include(authapp.urls)),
]
