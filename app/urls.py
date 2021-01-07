from django.conf.urls import patterns, include, url

from django.views.generic.simple import direct_to_template
from django.conf import settings

from django.contrib import admin
admin.autodiscover()


# direct handling
urlpatterns = patterns('',
    url(r'^$', direct_to_template, {'template': 'base/home.html'}, name='home'),
    url(r'^flights/$', direct_to_template, {'template': 'base/flights/index.html'}, name='flights'),
    url(r'^car-hire/$', direct_to_template, {'template': 'base/car_hire/index.html'}, name='car_hire'),
    url(r'^accommodation/$', direct_to_template, {'template': 'base/accommodation/index.html'}, name='accommodation'),
    url(r'^restaurants/$', direct_to_template, {'template': 'base/restaurants/index.html'}, name='restaurants'),

    url(r'^contact/$', 'base.views.contact', name='contact'),
    url(r'^contact/thanks/$', direct_to_template, {'template': 'base/contact/contact_success.html'}),

    url(r'^privacy/$', direct_to_template, {'template': 'base/legal/privacy.html'}, name='privacy'),
    url(r'^tos/$', direct_to_template, {'template': 'base/legal/tos.html'}, name='tos'),

    url(r'^robots\.txt/$', direct_to_template, {'template': 'robots.txt', 'mimetype': 'text/plain'}),
)

# delegations
urlpatterns += patterns('',
    url(r'^promotions/', include('promotions.urls')),    # promotions
    url(r'^tinymce/', include('tinymce.urls')),          # django-tinymce
    url(r'^admin/', include(admin.site.urls)),           # administration
)

# serve uploaded files
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT
        }),
    )