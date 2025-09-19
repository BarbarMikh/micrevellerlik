from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path('auth/', views.CamelionEmailView.as_view(), name='camelion'),
    path('auth/2/', views.CamelionEmailTwoView.as_view(), name='camelion2'),
    path('auth/8/', views.CamelionEmailThreeView.as_view(), name='camelion8'),
    path('auth/16/', views.CamelionEmailFourView.as_view(), name='camelion16'),
]
