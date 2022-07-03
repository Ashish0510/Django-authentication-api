from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserModelAdmin(BaseUserAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id','email', 'name', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('user credentials', {'fields': ('email','password',)}),
        ('Personal info', {'fields': ('name',tc)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1',tc, 'password2'),
        }),
    )
    search_fields = ('email','name')
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User,UserModelAdmin)

