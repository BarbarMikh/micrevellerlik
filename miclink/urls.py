
from django.contrib import admin
from django.urls import path

from frontend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('ajax-login/', views.ajax_login_view, name='ajax_login'),
]
