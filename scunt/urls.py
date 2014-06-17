from django.conf.urls import patterns, include, url
from django.contrib import admin
import os.path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'score.views.index'),
    url(r'^addscore1qazxsw23edcvfr45tgbnhy67ujm/', 'score.views.addscore'),
    url(r'^scoreboard/', 'score.views.scoreboard'),
    url(r'^admin1qazxsw23edcvfr45tgbnhy67ujm/', include(admin.site.urls)),
    url(r'^login1qazxsw23edcvfr45tgbnhy67ujm/', 'score.views.login'),
#	url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
#		{ 'document_root': os.path.join(os.path.dirname(__file__), '../scunt/static') }),
    # Examples:
    # url(r'^$', 'scunt_score.views.home', name='home'),
    # url(r'^scunt_score/', include('scunt_score.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()

