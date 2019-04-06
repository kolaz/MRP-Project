from django.contrib import admin
from system.models import Client, Supplier, ProductOrder, RawOrder


class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'surname', 'phone', 'created_at', )
    search_fields = ('name', 'surname', 'phone', )


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'surname', 'phone', 'created_at',)
    search_fields = ('name', 'surname', 'phone', )


class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'name', 'quantitiy', 'status', 'created_at', )
    search_fields = ('name', 'status', )


class RawOrderAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'name', 'quantitiy', 'status', 'created_at',)
    search_fields = ('name', 'status', )


admin.site.register(Client, ClientAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(ProductOrder, ProductOrderAdmin)
admin.site.register(RawOrder, RawOrderAdmin)
