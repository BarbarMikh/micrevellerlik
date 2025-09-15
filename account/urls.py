from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path('sign-in/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('log-details/<pk>/', views.log_details_view, name='log_details'),
]