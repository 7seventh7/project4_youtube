from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import test_app

from test_app.views import main_func


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('test_app.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)