from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=[
        ('chef', 'Chef'),
        ('cashier', 'Cashier'),
        ('manager', 'Manager'),
    ])

    def __str__(self):
        return self.user.username

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)  

    def __str__(self):
        return self.name


class Invoice(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Invoice #{self.id} - {self.date}"

class InvoiceItem(models.Model):
    invoice = models.ForeignKey("Invoice", on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey("MenuItem", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.unit_price is None:
            self.unit_price = self.item.price

        super().save(*args, **kwargs)

        total = sum(item.quantity * item.unit_price for item in self.invoice.items.all())
        self.invoice.total_amount = total
        self.invoice.save()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        total = sum(item.quantity * item.unit_price for item in self.invoice.items.all())
        self.invoice.total_amount = total
        self.invoice.save()

