from django.contrib import admin

from .models import Container, Channel, Transfer, Balance

class ContainerAdmin(admin.ModelAdmin):

    list_display_links = ('name', )
    list_display = ('user', 'name', 'currency')
    search_fields = ['^currency']
    fieldsets = (
        (None, {
            'fields': (
                 'user',
                 'name',
                 'currency',
            )
        }),
    )

class ChannelAdmin(admin.ModelAdmin):

    list_display_links = ('user', 'name', )
    list_display = ('user', 'name', 'source', 'destination')
    fieldsets = (
        (None, {
            'fields': (
                 'user',
                 'name',
                 'source',
                 'destination',
            )
        }),
    )

class TransferAdmin(admin.ModelAdmin):

    list_display_links = ('user', 'name', )
    list_display = ('user', 'name', 'channel',)
    fieldsets = (
        (None, {
            'fields': (
                 'user',
                 'name',
                 'channel',
                 ('start_time', 'start_value'),
                 ('end_time', 'end_value'),
            )
        }),
    )

class BalanceAdmin(admin.ModelAdmin):

    list_display_links = ('container', 'time', )
    list_display = ('container', 'time', )
    fieldsets = (
        (None, {
            'fields': (
                 'container',
                 'time',
                 'amount',
            )
        }),
    )

admin.site.register(Container, ContainerAdmin)
admin.site.register(Channel, ChannelAdmin)
admin.site.register(Transfer, TransferAdmin)
admin.site.register(Balance, BalanceAdmin)
