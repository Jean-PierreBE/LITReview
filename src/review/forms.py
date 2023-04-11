from django import forms
from review.models import Ticket, Review

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