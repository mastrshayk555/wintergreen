from django.contrib import admin
from .models import Budget, Category, Transactions

# Register your models here.
@admin.display(description="user")
def user_category(obj):
    return f"{obj.budget.user.first_name} {obj.budget.user.last_name}"

@admin.display(description="budget")
def category_budget(obj):
    return f"{obj.budget}"

@admin.display(description="user")
def transaction_user(obj):
    return f"{obj.category.budget.user}"

@admin.display(description="category")
def transaction_category(obj):
    return f"{obj.category}"

@admin.display(description="budget")
def transaction_budget(obj):
    return f"{obj.category.budget}"


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "name",
    )
    fields = [
        "name",
        "start_date",
        "end_date",
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        user_category,
        category_budget,
        "name",
    )
    fields = [
        "name",
        "budget",
    ]


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = (
        transaction_user,
        transaction_category,
        transaction_budget,
        "description",
        "amount",
    )
    fields = [
        "transaction_type",
        "description",
        "description_ext",
        "amount",
        "category",
        "date",
        "note",
    ]