from os import name
from django.urls import path
from . import views

app_name = "post"
urlpatterns = [       
    path('<slug:post>/', views.vista_post, name="vista_post"),
    path('page/<int:num>', views.vista_paginada, name="vista_paginada"),
    path('search/<str:query>', views.vista_busqueda, name="vista_busqueda"),
    path('search/<str:query>/page<int:num>', views.vista_busqueda, name="vista_busqueda_paginada")
]