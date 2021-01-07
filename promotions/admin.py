# Django admin
from django.contrib import admin
# django-tinymce dependencies
from django import forms
from tinymce.widgets import TinyMCE
# application models
from promotions.models import Promotion, Image


# TinyMCE form widgets

class PromotionForm(forms.ModelForm):
    text = forms.CharField(widget=TinyMCE(attrs={'cols': 100, 'rows': 18}))

    class Meta:
        model = Promotion


# inline models

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


# model display definitions

class PromotionAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'valid_from', 'expire_on', 'active',)
    list_editable = ('active',)
    list_filter = ('created', 'valid_from', 'expire_on', 'active',)

    search_fields = ('title', 'text',)

    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        ('Required (except \'Sub title\')',
            {'fields': ('title', 'sub_title', 'text',), 'description': 'Please enter this promotion\'s <em>title</em> and <em>description</em>.'}),
        ('Optional: Accommodation Details',
            {'fields': ('persons', 'nights', 'price'), 'description': 'Only required if this promotion involves accommodation.'}),
        ('Optional: General Details',
            {'fields': ('valid_from', 'expire_on', 'slug', 'active'), 'description': 'Check the <em>Active</em> box for this promotion to become eligible for public display.'})
    )

    inlines = [ImageInline]

    form = PromotionForm


class ImageAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'promotion',)

    fieldsets = (
        ('Required',
            {'fields': ('image', 'caption', 'promotion',)}),
        ('Optional',
            {'fields': ('title', 'alt',)})
    )


admin.site.register(Promotion, PromotionAdmin)
admin.site.register(Image, ImageAdmin)