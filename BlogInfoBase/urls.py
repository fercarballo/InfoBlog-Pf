from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from app.post.views import inicio_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", inicio_view), #esta ligada a app post
    path("", include("app.post.urls", namespace="Post"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
