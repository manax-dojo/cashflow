from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static 
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

urlpatterns = [

    # Multilingual
    url(r'^i18n/', include('django.conf.urls.i18n')),


    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, admin.site.urls),
 
    # Your stuff: custom urls includes go here 
 
 
 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

urlpatterns += i18n_patterns(

    # Homepage app
    url(r'^', include('homepage.urls')),  

    # User management
    url(r'^users/', include('users.urls', namespace='users')), 
    url(r'^accounts/', include('allauth.urls')), 

    # User avatar 
    url(r'^avatar/', include('avatar.urls')), 

    # Cashfield app
    url(r'^', include('cashfield.urls', namespace='cashfield')),  
)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ]

