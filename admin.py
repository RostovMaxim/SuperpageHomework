from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from .models import *


class NewFlatpageInline(admin.StackedInline):
    model = NewFlatpage
    verbose_name = "Содержание"

class FlatPageAdmin(FlatPageAdmin):
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': (
                'enable_comments',
                'registration_required',
                'template_name',
            ),
        }),
    )


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)