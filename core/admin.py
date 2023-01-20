from django.contrib import admin

from core.models import User, Messages


@admin.register(Messages)
class CountryAdmin(admin.ModelAdmin):
    readonly_fields = ('date_time',)


admin.site.register(User)
