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
            "followed_user",
        ]

    def clean(self):
        cleaned_data = super().clean()
        other_user = cleaned_data.get("followed_user")

        if other_user:
            # Only do something if both fields are valid so far.
            if other_user == get_user():
                raise ValidationError(
                    "Did not send for 'help' in the subject despite " "CC'ing yourself."
                )