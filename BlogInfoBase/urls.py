
from django.contrib import admin
from django.urls import path
from app.post.views import inicio_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", inicio_view) #esta ligada a app post
]
