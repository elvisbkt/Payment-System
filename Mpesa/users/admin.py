from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from .models import User, UserProfile, Role

admin.site.register(User, BaseUserAdmin)
admin.site.register(UserProfile)
admin.site.register(Role)


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
