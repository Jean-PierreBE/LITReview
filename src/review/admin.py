from django.contrib import admin
from review.models import Ticket, Review, UserFollows

class TicketAdmin(admin.ModelAdmin):
    pass

class ReviewAdmin(admin.ModelAdmin):
    pass

class UserFollowsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(UserFollows, UserFollowsAdmin)