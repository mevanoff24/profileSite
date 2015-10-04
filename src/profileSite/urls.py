from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'newsletter.views.home', name='home'),
	url(r'^contact/$', 'contact.views.contact', name='contact'),
    url(r'^about/$', 'profileSite.views.about', name='about'),
    url(r'^projects/$', 'project.views.projects', name='projects'),
    url(r'^projects/sabermetrics/$', 'project.views.sabermetrics', name='sabermetrics'),
    url(r'^projects/nycsubway/$', 'project.views.nycsubway', name='nycsubway'),
    url(r'^projects/playoffprediction/$', 'project.views.playoffprediction', name='playoffprediction'),
    url(r'^projects/enron/$', 'project.views.enron', name='enron'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^resume/$', 'profileSite.views.resume', name='resume'),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^accounts/', include('registration.backends.default.urls')),
]


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

