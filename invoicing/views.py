from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseForbidden, HttpResponse
from django.utils.timezone import now
from .models import Staff, MenuItem, Invoice, InvoiceItem

# Staff Login View
def staff_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and hasattr(user, 'staff'):
            login(request, user)
            role = user.staff.role
            if role == 'chef':
                return redirect('chef_dashboard')
            elif role == 'cashier':
                return redirect('cashier_dashboard')
            elif role == 'manager':
                return redirect('/admin/')
        else:
            return render(request, 'invoicing/login.html', {'error': 'Invalid login or not staff'})
    return render(request, 'invoicing/login.html')

# Chef Dashboard View
def chef_dashboard(request):
    if not hasattr(request.user, 'staff') or request.user.staff.role != 'chef':
        return HttpResponseForbidden("Access denied.")

    today = now().date()
    todays_orders = InvoiceItem.objects.filter(invoice__date=today)

    return render(request, 'invoicing/chef_dashboard.html', {
        'todays_orders': todays_orders
    })

# Cashier Dashboard View
def cashier_dashboard(request):
    if not hasattr(request.user, 'staff') or request.user.staff.role != 'cashier':
        return HttpResponseForbidden("Access denied.")

    recent_invoices = Invoice.objects.order_by('-date')[:5]

    return render(request, 'invoicing/cashier_dashboard.html', {
        'recent_invoices': recent_invoices
    })

# Manager Invoice View
def view_invoice(request):
    if not hasattr(request.user, 'staff'):
        return HttpResponseForbidden("Only staff members can access this.")
    if request.user.staff.role != 'manager':
        return HttpResponseForbidden("Only managers can view invoices.")
    
    return render(request, 'invoicing/invoices.html', {})
