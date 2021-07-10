from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from .models import Profile


class UserProfile(UserAdmin):
    list_display = ('username', 'email', 'phone', 'first_name', 'last_name', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (('Info'), {'fields': ('phone', 'avatar', 'gender')}),
    )


admin.site.register(Profile, UserProfile)


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["author"]


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["author"]
