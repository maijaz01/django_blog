from django.conf.urls import patterns, include, url
# from django.contrib import admin
import blog


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blog.views.HomeMassage', name='Homepage'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^about/$', 'blog.views.about', name='about'),
    url(r'^category/(?P<category_name>[\w\-]+)/$', 'blog.views.category', name='category'),)

    # url(r'^admin/', include(admin.site.urls))

