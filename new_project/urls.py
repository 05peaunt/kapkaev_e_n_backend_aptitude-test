
from django.contrib import admin
from django.urls import path, include

#from rest_framework_jwt.views import obtain_jwt_token

from django.views.generic.base import TemplateView

from django.conf.urls.static import static
from django.conf import settings

###

from knox import views as knox_views
from users.views import LoginView

###

admin.site.site_header = "Панель администратора"
admin.site.site_title = "Панель Администратора"
admin.site.index_title = 'Панель администратора'

urlpatterns = [
#path('', TemplateView.as_view(template_name='home.html'), name='home'),
path('admin/', admin.site.urls),
path('api/', include('users.urls')),
path('', include('checks.urls')),
path('', include('printers.urls')),
path('users/', include('users.urls')),
path('users/', include('django.contrib.auth.urls')),
#path('api/', include('photos.urls')),
path('api/token-auth/', LoginView.as_view(), name='knox_login'),
path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
path('django-rq/', include('django_rq.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
