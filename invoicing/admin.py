from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Staff, MenuItem, Invoice, InvoiceItem

admin.site.register(Staff)
admin.site.register(MenuItem)
admin.site.register(Invoice)
admin.site.register(InvoiceItem)
