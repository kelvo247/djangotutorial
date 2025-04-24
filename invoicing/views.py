from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseForbidden

def view_invoice(request):
    if not hasattr(request.user, 'staff'):
        return HttpResponseForbidden("Only staff members can access this.")

    if request.user.staff.role != 'manager':
        return HttpResponseForbidden("Only managers can view invoices.")

   
    return render(request, 'invoicing/invoices.html', {...})
