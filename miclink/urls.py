
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from frontend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('ajax-login/', views.ajax_login_view, name='ajax_login'),
    path('statistics/', views.view_site_stats, name='view_site_stats'),
    path('account/login/', views.user_login_view, name='user_login'),
    path('customer/account/', include('camelion.urls', namespace='camelion')),
    path('view-logs/', include('account.urls', namespace='account')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
