from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from fortytwo_test_task.settings import STATIC_URL, STATIC_ROOT
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'hello.views.main_page', name='home'),
)
urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
