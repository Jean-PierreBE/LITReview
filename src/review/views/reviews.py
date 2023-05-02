from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import View
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from review.forms import ReviewFormLast, ReviewFormFirst, ReviewForm
from review.models import Review, Ticket
from django.contrib import messages
# Create your views here.

class review_delete(DeleteView):
    model = Review
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            messages.success(self.request, "La critique a bien été supprimée")
        return super().form_valid(form)

class review_create(CreateView):
    template_name = 'review/edit_review.html'
    form_class = ReviewForm
    model = Review
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        ticket = get_object_or_404(Ticket, pk=self.kwargs['ticket_pk'])
        context["title"] = "Créer une critique"
        context["action"] = "envoyer"
        context["ticket"] = ticket
        return context
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            ticket = get_object_or_404(Ticket, pk=self.kwargs['ticket_pk'])
            form.instance.user = self.request.user
            form.instance.ticket_id = ticket.id
            messages.success(self.request, "La critique a bien été créee")
        return super().form_valid(form)

class review_update(UpdateView):
    template_name = 'review/edit_review.html'
    form_class = ReviewForm
    model = Review
    success_url = reverse_lazy('posts')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        ticket = get_object_or_404(Ticket, pk=self.object.ticket_id)
        context["title"] = "Modifier votre critique"
        context["action"] = "envoyer"
        context["ticket"] = ticket
        return context
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            messages.success(self.request, "La critique a bien été mise à jour")
        return super().form_valid(form)

class OwnReview_create(View):

    template_name = 'review/crud_review.html'
    form01 = ReviewFormFirst
    form02 = ReviewFormLast

    def get(self, request):
        form01 = self.form01()
        form02 = self.form02()
        return render(request,
                      self.template_name,
                      {"title": "Créer une critique","action":"créer","sub_title01":"livre/Article","sub_title02":"Critique",
                       "form01": form01,"form02": form02})

    def post(self, request, *args, **kwargs):
        form01 = self.form01(request.POST, request.FILES)
        form02 = self.form02(request.POST)
        errors = []
        if form01.is_valid() and form02.is_valid():
            # create ticket
            ticket = Ticket()
            ticket.user = self.request.user
            ticket.title = form01.cleaned_data["rev_title"]
            ticket.description = form01.cleaned_data["rev_description"]
            ticket.image = form01.cleaned_data["rev_image"]
            # create review
            review = Review()
            review.user = self.request.user
            review.rating = form02.cleaned_data["rev_rating"]
            review.headline = form02.cleaned_data["rev_headline"]
            review.body = form02.cleaned_data["rev_body"]
            if not errors:
                ticket.save()
                review.ticket_id = ticket.id
                review.save()
                messages.add_message(request, messages.SUCCESS, "La critique a été créée avec succès!!")
                return redirect('create_own_review')
            else:
                for error in errors:
                    messages.add_message(request, messages.ERROR, error)
                return redirect('create_own_review')
