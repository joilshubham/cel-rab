from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Item, ItemAdmin)