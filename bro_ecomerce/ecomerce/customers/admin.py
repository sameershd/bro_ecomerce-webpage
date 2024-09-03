from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'delete_status', 'create_at', 'update_at')
    list_filter = ('delete_status', 'create_at')
    search_fields = ('name', 'phone')
    ordering = ('-create_at',)
    readonly_fields = ('create_at', 'update_at')
    fieldsets = (
        (None, {
            'fields': ('name', 'adddress', 'user', 'phone', 'delete_status')
        }),
        ('Timestamps', {
            'classes': ('collapse',),
            'fields': ('create_at', 'update_at'),
        }),
    )

admin.site.register(Customer, CustomerAdmin)
