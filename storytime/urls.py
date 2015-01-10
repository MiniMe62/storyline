from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     url(r'^admin/', include(admin.site.urls)),
#     url(r'^$', 'story.views.home', name='home'),
#    (r'^admin/', include(admin.site.urls)),
#    (r'^$', 'story.views.home', name='home'),
    # Examples:
    # url(r'^$', 'storytime.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
)
