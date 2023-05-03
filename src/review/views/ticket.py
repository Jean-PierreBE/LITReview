from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from review.forms import TicketForm
from review.models import Ticket
from django.contrib import messages
# Create your views here.


class ticket_delete(DeleteView):
    model = Ticket
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            messages.success(self.request, "Le ticket a bien été supprimé")
        return super().form_valid(form)


class ticket_update(UpdateView):
    template_name = 'review/crud_ticket.html'
    form_class = TicketForm
    model = Ticket
    success_url = reverse_lazy('posts')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["title"] = "Modification d'un ticket"
        context["action"] = "envoyer"
        return context

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            messages.success(self.request, "Le ticket a bien été mis à jour")
        return super().form_valid(form)


class CreateTicketView(CreateView):

    model = Ticket
    template_name = 'review/crud_ticket.html'
    form_class = TicketForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["title"] = "Créer un ticket"
        context["action"] = "Envoyer"
        return context

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)
