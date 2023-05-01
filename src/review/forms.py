from django import forms
from review.models import Ticket, Review, UserFollows
from django.contrib.auth import get_user

RATING_CHOICES = [('0', ' 0'), ('1', ' 1'), ('2', ' 2'), ('3', ' 3'), ('4', ' 4'), ('5', ' 5')]

class ReviewFormFirst(forms.Form):
    rev_title = forms.CharField(label="Titre", widget=forms.TextInput())
    rev_description = forms.CharField(label="Description", widget=forms.Textarea)
    rev_image = forms.ImageField(label="Image")

class ReviewFormLast(forms.Form):
    rev_headline = forms.CharField(label="Titre", widget=forms.TextInput())
    rev_rating = forms.ChoiceField(label="Note", widget=forms.RadioSelect(attrs={'class': 'inline'}),initial='3',choices=RATING_CHOICES)
    rev_body = forms.CharField(label="Commentaire", widget=forms.Textarea)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "headline",
            "rating",
            "body",
        ]
        widgets = {
            "rating": forms.RadioSelect(attrs={'class': 'inline'},choices=RATING_CHOICES)
        }
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            "title",
            "description",
            "image",
        ]

class UserFollowsForm(forms.Form):
    followed_name = forms.CharField(label="Utilisateur" ,widget = forms.TextInput())
