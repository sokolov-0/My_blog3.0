from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from mozilla_django_oidc.urls import urlpatterns as oidc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.blog_app.urls')),
    
    path('accounts/oidc/', include('mozilla_django_oidc.urls')),
    path('accounts/', include(('app.accounts.urls', 'accounts'), namespace='accounts')),
    #path('accounts/', include(('app.accounts.urls', 'accounts'))),
]

print(oidc_urls)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
