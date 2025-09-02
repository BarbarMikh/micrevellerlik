
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from frontend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('ajax-login/', views.ajax_login_view, name='ajax_login'),
    path('statistics/', views.view_site_stats, name='view_site_stats'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
