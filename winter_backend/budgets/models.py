from django.db import models

from accounts.models import User

# Create your models here.

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
    

class Category(models.Model):
    class Meta: 
        verbose_name = "category"
        verbose_name_plural = "categories"

    name = models.CharField(max_length=100)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    

class Transactions(models.Model):
    class Meta:
        verbose_name = "transaction"
        verbose_name_plural = "transactions"


    debit = 'D'
    credit = 'C'
    TRANS_TYPE_CHOICES = {
        debit: 'DEBIT',
        credit: 'CREDIT'
    }
    transaction_type = models.CharField(max_length=20, choices=TRANS_TYPE_CHOICES)
    description = models.CharField(max_length=200)
    description_ext = models.CharField(max_length=200)
    amount = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    transaction_date = models.DateField()
    note = models.TextField()
    
    def __str__(self):
        return self.description
    