from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, CreateView, View
from django.urls import reverse_lazy
from review.forms import TicketForm
from review.models import Ticket
from connexion.models import ConnectUser
from django.contrib import messages
from itertools import chain
from django.conf import settings
# Create your views here.

def ticket_del(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)

    if request.method == 'POST':
        ticket.delete()
        messages.add_message(request, messages.SUCCESS, "Le ticket a bien été supprimé")
        return redirect('posts')

def ticket_update(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)

    if request.method == 'POST':
        edit_ticket = TicketForm(request.POST, request.FILES, instance=ticket)
        if edit_ticket.is_valid():
            edit_ticket.save()
            return redirect('posts')
    else:
        edit_ticket = TicketForm(instance=ticket)

    context = {
        'form': edit_ticket,
        'title': "Modification d'un ticket",
        'action': "Modifier",
    }
    return render(request, 'review/crud_ticket.html', context=context)

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
