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
class HomeView(TemplateView):
    template_name = 'review/home.html'
