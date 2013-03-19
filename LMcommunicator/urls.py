from django.conf.urls import patterns, include, url
from django.contrib.auth import authenticate
from LMcommunicator import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
	                   '',
	                   #url(r'^LMcommunicator/', include('LMcommunicator.urls', namespace='LMcommunicator')),
                       url(r'^$', views.home, name='home'),
                       url(r'^graph/$', views.graph, name='graph'),
                       url(r'^graph_chart/$', views.graph_chart, name='graph_chart'),
    # Examples:
    # url(r'^$', 'LMcommunicator.views.home', name='home'),
    # url(r'^LMcommunicator/', include('LMcommunicator.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
