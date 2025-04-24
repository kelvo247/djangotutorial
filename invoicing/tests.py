from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Staff, MenuItem, Invoice, InvoiceItem

class InvoiceTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='kelvo')
        self.staff = Staff.objects.create(user=self.user, role='cashier')
        self.item = MenuItem.objects.create(name='Test Item', unit_price=4.50)
        self.invoice = Invoice.objects.create(staff=self.staff)
        self.invoice_item = InvoiceItem.objects.create(invoice=self.invoice, item=self.item, quantity=2)

    def test_invoice_total_amount_calculation(self):
        self.invoice.refresh_from_db()
        self.assertEqual(self.invoice.total_amount, 9.00)

    def test_invoice_item_auto_unit_price(self):
        self.assertEqual(self.invoice_item.unit_price, 4.50)

class MenuItemTests(TestCase):
    def test_menu_item_creation(self):
        item = MenuItem.objects.create(name='Burger', unit_price=5.99)
        self.assertEqual(item.name, 'Burger')
        self.assertEqual(item.unit_price, 5.99)