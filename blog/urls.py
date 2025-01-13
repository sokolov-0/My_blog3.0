from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from django_keycloak.views import Login, Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('app.blog_app.urls', 'blog_app'), namespace='blog_app')),
    #path('accounts/', include(('app.accounts.urls', 'accounts'), namespace='accounts')),
    path('keycloak/', include('django_keycloak.urls', namespace='keycloak')),
    # path('keycloak/login/', Login.as_view(), name='login'),
    # path('accounts/logout/', Logout.as_view(), name='logout'),
]



#print(oidc_urls)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
