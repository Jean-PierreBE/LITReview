from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from review.forms import UserFollowsForm
from review.models import UserFollows
from connexion.models import ConnectUser
from django.contrib import messages
# Create your views here.
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
