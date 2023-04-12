from django.contrib import admin
from review.models import Ticket

class TicketAdmin(admin.ModelAdmin):
    pass


admin.site.register(Ticket, TicketAdmin)