# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserLegalInfo, UserContactDetail, Bank, UserBank

class UserLegalInfoInline(admin.StackedInline):
    model = UserLegalInfo
    can_delete = False

class UserContactDetailInline(admin.TabularInline):
    model = UserContactDetail
    extra = 1

class UserBankInline(admin.TabularInline):
    model = UserBank
    extra = 1

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'middle_name', 'last_name', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    inlines = (UserLegalInfoInline, UserContactDetailInline, UserBankInline)
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('middle_name',)}),
    )

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('name', 'acronym', 'address')
    search_fields = ('name', 'acronym')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(UserContactDetail)
class UserContactDetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_of', 'number', 'email')
    search_fields = ('name', 'number', 'email')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(UserBank)
class UserBankAdmin(admin.ModelAdmin):
    list_display = ('user', 'bank', 'account_number')
    search_fields = ('user__username', 'bank__name', 'account_number')