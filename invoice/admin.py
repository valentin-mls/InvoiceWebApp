from django.contrib import admin
from .models import *

# admin.site.register(Client)
admin.site.register(Product)
# admin.site.register(Invoice)
admin.site.register(Settings)


class ClientAdmin(admin.ModelAdmin):
    search_fields= ('clientName'),
    ordering= ["clientName"]

class InvoiceAdmin(admin.ModelAdmin):
    ordering= ['title']
    autocomplete_fields = ['client']

admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Client, ClientAdmin)