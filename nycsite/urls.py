from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nycsite.views.home', name='home'),
    # url(r'^nycsite/', include('nycsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('webapp.views',
                       url(r'^home/$', 'home', name = 'home'),
                       url(r'^/$', 'home', name = 'home'),
                       url(r'^community/$', 'community', name = 'community'),
)