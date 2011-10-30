# -*- coding: utf-8 -*-
from django.db import models
from django import forms
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.template.context import RequestContext
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

"""
# Here are some example customization methods:
DEMO_SETTINGS = (
     ('foo', _('Foo')),
     ('bar', _('Bar'))          
)
DEMO_CHOICES = (
    ('red', _('Take the red pill')),
    ('blue'. _('Take the blue pill'))
)


class MyContent(models.Model):
    # This content is just for quick reference.
    
    @classmethod
    def initialize_type(cls, CONTENT_SETTINGS=DEMO_SETTINGS, TYPE_CHOICES=DEMO_CHOICES):
        #    Use this function like a constructor for your content. Attributes
        #    that are defined here are available in all instances of the content.
        #    Set those attributes as arguments in the Page.create_content_type function.

        cls.CONTENT_SETTINGS = CONTENT_SETTINGS
        
        #    You can even add new fields to the class that have user-definable
        #    attributes.
        
        cls.add_to_class('answer', models.CharField(max_length=20, choices=TYPE_CHOICES, default='red'))


    class Meta:
        abstract = True
        verbose_name = _('My great Content')
        verbose_name_plural = _('My great Contents')
    

    def __unicode__(self):
        return u'Demo Content'


    def render(self, request, **kwargs):
        # do something here
        return render_to_string('template.html', {'foo': 'bar' }, RequestContext(request))


    @property
    def media(self):
        #    This property lets you define static media files that are included only
        #    when the content is active on your site. Don't forget to add the 
        #    {{ feincms_page.media.js }} and {{ feincms_page.media.css }} tags.
        #    By default the path is added to STATIC_URL. If you need to customize
        #    the media files use MEDIA_URL prefix shown below.

        return forms.Media(
            css={'all' : ('%scontent/baseapp/baseapp.css' % settings.MEDIA_URL,),},
            js=('js/jquery.hoverintent.minified.js',
                '%scontent/baseapp/baseapp.js' % settings.MEDIA_URL,
                )
        )
"""


