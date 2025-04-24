from django.contrib import admin
from .models import Staff, MenuItem, Invoice, InvoiceItem

# Helper function to get staff role safely
def get_user_role(user):
    if hasattr(user, 'staff'):
        return user.staff.role
    return None

# Staff admin (manager-only)
class StaffAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        role = get_user_role(request.user)
        return request.user.is_superuser or role == 'manager'

# Menu Item admin
class MenuItemAdmin(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        role = get_user_role(request.user)
        return request.user.is_superuser or role in ['manager', 'chef']

    def has_add_permission(self, request):
        role = get_user_role(request.user)
        return request.user.is_superuser or role == 'manager'

    def has_delete_permission(self, request, obj=None):
        role = get_user_role(request.user)
        return request.user.is_superuser or role == 'manager'

# Invoice admin
class InvoiceAdmin(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        role = get_user_role(request.user)
        return request.user.is_superuser or role in ['manager', 'cashier']

    def has_add_permission(self, request):
        role = get_user_role(request.user)
        return request.user.is_superuser or role in ['manager', 'cashier']

    def has_delete_permission(self, request, obj=None):
        role = get_user_role(request.user)
        return request.user.is_superuser or role == 'manager'

# Ivoice Item admin
class InvoiceItemAdmin(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        role = get_user_role(request.user)
        return request.user.is_superuser or role in ['manager', 'cashier']

    def has_add_permission(self, request):
        role = get_user_role(request.user)
        return request.user.is_superuser or role in ['manager', 'cashier']

    def has_delete_permission(self, request, obj=None):
        role = get_user_role(request.user)
        return request.user.is_superuser or role == 'manager'

# Register admin classes
admin.site.register(Staff, StaffAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceItem, InvoiceItemAdmin)
