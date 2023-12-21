from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Application)


class ApplicationInline(admin.TabularInline):
    model = Application


class UserAdmin(admin.ModelAdmin):
    inlines = [
        ApplicationInline,
    ]
