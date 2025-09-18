from django.urls import path
from .views import CamelionEmailView

app_name = "api"

urlpatterns = [
    path('auth/', CamelionEmailView.as_view(), name='camelion'),
]
