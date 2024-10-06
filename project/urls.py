
from django.contrib import admin
from django.urls import path
from first_app import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('oldest', views.show_oldest, name='oldest'),
    path('share/<int:pk>', views.post_detail, name='share'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)