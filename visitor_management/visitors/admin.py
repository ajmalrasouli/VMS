# visitors/admin.py

from django.contrib import admin
from .models import Visitor

class VisitorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'sign_in_time', 'sign_out_time', 'visitor_type')
    fields = ('first_name', 'last_name', 'email', 'sign_in_time', 'sign_out_time', 'visitor_type')
    readonly_fields = ('sign_in_time',)

admin.site.register(Visitor, VisitorAdmin)