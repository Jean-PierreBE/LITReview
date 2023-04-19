from django import forms
from review.models import Ticket, Review, UserFollows
from django.contrib.auth import get_user

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "headline",
            "rating",
            "body",
        ]

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            "title",
            "description",
            "image",
        ]

class UserFollowsForm(forms.ModelForm):
    class Meta:
        model = UserFollows
        fields = [
            'followed_user',
        ]
