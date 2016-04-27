from django.contrib import admin

from .models import Ambito, Spesa, Tag

class AmbitoAdmin(admin.ModelAdmin):
    list_display = ('descrizione', 'num')
    ordering = ['num']

class SpesaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Date', {
            'fields': (
                'data_accredito',
                'data_riferimento',
            ),
            # 'classes': ['collapse']
        }),
        ('Dettagli', {
            'fields': [
                'ambito',
                'importo',
                'descrizione',
                'quantita',
            ],
        }),
        ('Tags', {
            'fields': [
                'tags',
            ],
        }),
    ]
    list_display = ('data_accredito', 'importo', 'descrizione', 'ambito')
    list_filter = [
        'data_accredito',
        'data_riferimento',
        'ambito',
        'tags',
    ]
    filter_horizontal = ['tags']
    search_fields = ['descrizione']


admin.site.register(Ambito, AmbitoAdmin)
admin.site.register(Spesa, SpesaAdmin)
admin.site.register(Tag)
