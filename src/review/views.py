from django.shortcuts import render, HttpResponseRedirect, redirect
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.views import View
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from review.forms import TicketForm, UserFollowsForm
from review.models import Ticket, UserFollows
from connexion.models import ConnectUser
from django.contrib import messages

# Create your views here.
class HomeView(TemplateView):
    template_name = 'review/home.html'

class PostsView(View):
    template_name = 'review/posts.html'
    title01 = "default"
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["title01"] = self.title01
        return context

    def get(self, request):
        return render(request, self.template_name)
class UserFollowsView(CreateView):
    model = UserFollows
    template_name = 'review/abonnements.html'
    form_class = UserFollowsForm
    success_url = reverse_lazy('home')
    title01 = "default"
    title02 = "default"
    title03 = "default"
    action01 = "default"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["title01"] = self.title01
        context["title02"] = self.title02
        context["title03"] = self.title03
        context["action01"] = self.action01
        context["follows"] = UserFollows.objects.filter(user=self.request.user)
        context["followers"] = UserFollows.objects.filter(followed_user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        form = UserFollowsForm(request.POST)
        errors = []
        if form.is_valid():
            form.instance.user = self.request.user
            if self.request.user == form.instance.followed_user:
                errors.append("Un utilisateur ne peut se suivre lui-même!")
            if UserFollows.objects.filter(user=self.request.user, followed_user=form.instance.followed_user).exists():
                errors.append("Le couple "+ str(self.request.user) + " et "+ str(form.instance.followed_user) + " existe déja !!")
            if not errors:
                form.save()
                messages.add_message(request, messages.SUCCESS, "Le couple "+ str(self.request.user) + ","+ str(form.instance.followed_user) + " a été créé avec succès!!")
                return redirect('abonnements')
            else:
                for error in errors:
                    messages.add_message(request, messages.ERROR, error)
                    print(messages.ERROR)
                return redirect('abonnements')

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
