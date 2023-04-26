from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.views import View
from django.views.generic import TemplateView, CreateView, View
from django.urls import reverse_lazy
from review.forms import TicketForm, UserFollowsForm, ReviewFormLast, ReviewFormFirst
from review.models import Ticket, UserFollows, Review
from connexion.models import ConnectUser
from django.contrib import messages
from itertools import chain
from django.conf import settings
# Create your views here.

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
