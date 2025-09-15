from django.urls import path
from . import views

app_name = "camelion"

urlpatterns = [
    path('view-profile/', views.camelion_view, name='camelion'),
]