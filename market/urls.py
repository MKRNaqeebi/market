"""market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),

    # Messaging app
    path('messaging/', include('market.apps.messaging.urls')),

    # Remove logout confirmation
    # Note: Needs to be changed to redirect to ACCOUNT_LOGOUT_REDIRECT_URL
    # url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    path('accounts/', include('allauth.urls')),

    # Social app
    path('', include('market.apps.social.urls')),

    # Board app
    path('', include('market.apps.board.urls')),

]

# URL for media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
