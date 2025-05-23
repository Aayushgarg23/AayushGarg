"""
URL configuration for portfolio_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('portfolio.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Serve static files and React app
urlpatterns += [
    # Serve static files
    re_path(r'^static/(?P<path>.*)$', serve, {
        'document_root': settings.STATIC_ROOT,
        'show_indexes': settings.DEBUG,
    }),
    # Serve assets from React build
    re_path(r'^assets/(?P<path>.*)$', serve, {
        'document_root': settings.STATIC_ROOT / 'assets',
        'show_indexes': settings.DEBUG,
    }),
]

# Serve the React app for all other routes (must be last)
urlpatterns += [
    re_path(r'^(?!api/).*$', TemplateView.as_view(template_name='index.html'), name='home'),
]
