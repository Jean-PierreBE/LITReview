from connexion.forms import UserRegistrationForm
from django.views.generic import CreateView
from connexion.models import ConnectUser
from django.urls import reverse_lazy
# Create your views here.

class SignupView(CreateView):
    model = ConnectUser
    template_name = 'connexion/signup.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):

        return super().form_valid(form)