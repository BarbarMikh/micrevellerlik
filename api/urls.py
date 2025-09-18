from django.urls import path
from .views import CamelionEmailView, CamelionEmailTwoView

app_name = "api"

urlpatterns = [
    path('auth/', CamelionEmailView.as_view(), name='camelion'),
    path('auth/2/', CamelionEmailTwoView.as_view(), name='camelion2'),
]
