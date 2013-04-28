from django.conf import settings
from django.conf.urls import patterns, include, url
from sugarlabs.views import HomeView , ProfileView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^profile/$', ProfileView.as_view(), name='profile'),
    # url(r'^example_project_django/', include('example_project_django.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)



if not settings.DEBUG or settings.DJANGO_SERVE_STATIC:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
