# -*- coding: utf-8 -*-
from django.contrib import admin

"""
This demo admin class shows you how to add TinyMCE to a textarea and use language-aware
inlines:


from django import forms
from feincms import translations

from models import Demo, DemoTranslation

class TinyMCEAdminForm(forms.ModelForm):
    # Use this form class if you want to add TinyMCE to a text input.
    class Meta:
        widgets = {
            'text': forms.widgets.Textarea(attrs={'class':'vLargeTextField tinymce'}),
        }


class DemoAdmin(admin.ModelAdmin):
    # Add the TinyMCE Form class for TinyMCE support:
    form = TinyMCEAdminForm
    list_display = ('name', )
    # For multi-language apps add language-aware inlines.
    # raw_id foreign key to page opens a nice tree view and lets you select a page.
    inlines=[translations.admin_translationinline(DemoTranslation, raw_id_fields = ('page',),
                                                   form=TinyMCEAdminForm)]
    
    class Media:
        # add the TinyMCE Java scripts
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.6.1/jquery.min.js',
            'tinymce/tiny_mce.js',
            'tinymce_admin/init.js',
        )

admin.site.register(Demo, DemoTranslation)
"""