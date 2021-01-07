from datetime import datetime, date, timedelta
from django.db import models
from django.core.urlresolvers import reverse


# auxiliary managers

class PromotionManager(models.Manager):
    def get_query_set(self):
        default_query_set = super(PromotionManager, self).get_query_set()
        return default_query_set.filter(expire_on__gte=datetime.now(), valid_from__lte=datetime.now(), active=True)

# begin models

class Promotion(models.Model):
    title = models.CharField(max_length=255, help_text='The name of your promotion.')
    sub_title = models.CharField(max_length=255, blank=True, help_text='Example: "15% discount for all bookings made through Example.com!"')
    slug = models.SlugField(help_text='Search engine-friendly URL (default: auto-generated from <em>title</em> field).')
    text = models.TextField()
    nights = models.IntegerField(blank=True, null=True, help_text='Amount of accommodation nights on offer.')
    persons = models.IntegerField(blank=True, null=True, help_text='Amount of people which can be accommodated.')
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True, help_text='The price in decimal ZAR, sans the "R" eg: 395.99')
    active = models.BooleanField(default=False, help_text='Activate to display publicly on Example.com (default: <em>not</em> active)')
    created = models.DateTimeField(auto_now_add=True)
    valid_from = models.DateField(default=date.today, help_text='When this promotion will become visible on the site (default: today).')
    expire_on = models.DateField(default=lambda: date.today() + timedelta(days=30), help_text='When this promotion will be removed from the site (default: 30 days from today) (remains in the database for future use).')

    class Meta:
        verbose_name_plural = 'promotions'

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('promotion', args=(self.slug,))

    # 1st, becomes default manager - for admin etc
    _objects = models.Manager()
    # 2nd, explicit name override - for views & URLconfs
    objects = PromotionManager()

class Image(models.Model):
    image = models.ImageField(upload_to='promotions/images', help_text='Add an image to this promotion. Width: 440px, Height: 200px')
    caption = models.CharField(max_length=255, help_text='Enter a description that will be displayed with your image.')
    promotion = models.ForeignKey(Promotion, related_name='images', help_text='Choose a promotion with which to display this image.')
    title = models.CharField(max_length=255, blank=True, help_text='For the <strong><em>title</em></strong> attribute of HTML\'s <em>img</em> element.')
    alt = models.CharField(max_length=255, blank=True, help_text='For the <strong><em>alt</em></strong> attribute of HTML\'s <em>img</em> element.')

    def __unicode__(self):
        return self.image.name

    def get_absolute_url(self):
        return reverse('django.views.static.serve', kwargs={'path': self.image.name})
