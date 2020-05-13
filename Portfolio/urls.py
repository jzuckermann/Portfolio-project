
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
import jobs.views
import app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("authentication.urls")),
    path('', include("app.urls")),
    path('blog/', include('blog.urls')),
    path('theme/', jobs.views.theme),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
