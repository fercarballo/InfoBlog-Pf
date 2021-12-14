from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from app.post.views import inicio_view, registro
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/',registro, name="registro"),
    path("", inicio_view, name = "inicio"), #esta ligada a app post
    path("", include("app.post.urls", namespace="Post")),
    path('accounts/', include('django.contrib.auth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
