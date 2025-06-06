from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView
from .views.views import HomeView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view(), name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += [
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html'))
]