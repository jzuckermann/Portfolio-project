
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
import jobs.views
import app.views
import contact.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("authentication.urls")),
    path('', include("app.urls")),
    path('blog/', include('blog.urls')),
    path('ui-contact-us.html', contact.views.Contact)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
