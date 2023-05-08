from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from review.forms import UserFollowsForm
from review.models import UserFollows
from connexion.models import ConnectUser
from django.contrib import messages
# Create your views here.


class follow_user_delete(DeleteView):
    model = UserFollows
    success_url = reverse_lazy('abonnements')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            messages.success(self.request, "L'utilisateur a bien été retiré de vos abonnements")
        return super().form_valid(form)


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
                errors.append("Aucun utilisateur ne correspond à ce pseudo.")
            if len(errors) == 0:
                if self.request.user == followed_user:
                    errors.append("Un utilisateur ne peut se suivre lui-même!")
                if UserFollows.objects.filter(user=self.request.user, followed_user=followed_user).exists():
                    errors.append("Vous suivez déja " + str(followed_user) + " !!")
            if not errors:
                follow.followed_user = followed_user
                follow.save()
                messages.add_message(request, messages.SUCCESS, "Vous suivez maintenant " + str(followed_user) + " !!")
                return redirect('abonnements')
            else:
                for error in errors:
                    messages.add_message(request, messages.ERROR, error)
                return redirect('abonnements')
