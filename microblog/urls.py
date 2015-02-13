from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views
from django.conf import settings
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'microblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r"^$", views.HomepageView.as_view(), name="home"), 
    url(r"^blog/", include("blog.urls", namespace="blog")),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^static/(.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT
                }),
)
