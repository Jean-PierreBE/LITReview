from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.views import View
from django.views.generic import TemplateView, CreateView, View
from django.urls import reverse_lazy
from review.forms import TicketForm, UserFollowsForm, ReviewFormFirst, ReviewFormLast
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

def follow_user_del(request, pk):
    follow = get_object_or_404(UserFollows, pk=pk)  # Get your current cat

    if request.method == 'POST':  # If method is POST,
        follow.delete()  # delete the cat.
        messages.add_message(request, messages.SUCCESS, "L'utilisateur a bien été retiré de vos abonnements")
        return redirect('abonnements')


class UserFollowsView(View):
    template_name = 'review/abonnements.html'
    form = UserFollowsForm
    success_url = reverse_lazy('home')

    def get(self, request):
        form = self.form()
        follows = UserFollows.objects.filter(user=self.request.user)
        followers = UserFollows.objects.filter(followed_user=self.request.user)

        return render(request,
                      self.template_name,
                      {"follows": follows,
                       "form": form,
                       "followers": followers})
    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        errors = []
        if form.is_valid():
            follow = UserFollows()
            follow.user = self.request.user
            followed_name = form.cleaned_data["followed_name"]
            try:
                followed_user = ConnectUser.objects.get(pseudo=followed_name)
            except ConnectUser.DoesNotExist:
                errors.append("Aucun user ne correspond à ce nom.")
            if len(errors) == 0:
                if self.request.user == followed_user:
                    errors.append("Un utilisateur ne peut se suivre lui-même!")
                if UserFollows.objects.filter(user=self.request.user, followed_user=followed_user).exists():
                    errors.append("Le couple "+ str(self.request.user) + " et "+ str(followed_user) + " existe déja !!")
            if not errors:
                follow.followed_user = followed_user
                follow.save()
                messages.add_message(request, messages.SUCCESS, "Le couple "+ str(self.request.user) + ","+ str(followed_user) + " a été créé avec succès!!")
                return redirect('abonnements')
            else:
                for error in errors:
                    messages.add_message(request, messages.ERROR, error)
                return redirect('abonnements')

class ReviewView(View):

    template_name = 'review/crud_review.html'
    form01 = ReviewFormFirst
    form02 = ReviewFormLast
    success_url = reverse_lazy('home')

    def get(self, request):
        form01 = self.form01()
        form02 = self.form02()
        return render(request,
                      self.template_name,
                      {"title": "Créer une critique","action":"créer","sub_title01":"livre/Article","sub_title02":"Critique",
                       "form01": form01, "form02": form02})

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
