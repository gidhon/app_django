from django.conf.urls import patterns, include, url


urlpatterns = patterns('promotions.views',
    # list all specials
    url(r'^$', 'promotions', name='promotions'),
    # detail a special
    url(r'^(?P<slug>[-\w]+)/$', 'promotion', name='promotion'),
)