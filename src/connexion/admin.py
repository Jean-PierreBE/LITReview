from django.contrib import admin # noqa : F401
from connexion.models import ConnectUser


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(ConnectUser, UserAdmin)
