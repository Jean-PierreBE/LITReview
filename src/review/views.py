from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from review.forms import TicketForm
from review.models import Ticket

# Create your views here.
class HomeView(TemplateView):
    template_name = 'review/home.html'

class PostsView(View):
    def get(self, request):
        return render(request, 'review/posts.html')

class AbonnementsView(View):
    def get(self, request):
        return render(request, 'review/abonnements.html')

class ReviewView(View):
    def get(self, request):
        return render(request, 'review/crud_review.html')

class CreateTicketView(CreateView):
    model = Ticket
    template_name = 'review/crud_ticket.html'
    form_class = TicketForm
    success_url = reverse_lazy('home')
    title = "default"
    action = "default"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["title"] = self.title
        context["action"] = self.action
        return context
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)
