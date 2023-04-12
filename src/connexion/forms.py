from django.contrib.auth.forms import UserCreationForm
from connexion.models import ConnectUser
from django.forms import TextInput

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = ConnectUser
        fields = ("pseudo", "email", )