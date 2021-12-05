from django.urls import path
from . import views

app_name = "post"
urlpatterns = [       
    path('<slug:post>/', views.vista_post, name="vista_post"),    
]