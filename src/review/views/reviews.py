from django.shortcuts import render, redirect
from django.views import View
from review.forms import ReviewFormLast, ReviewFormFirst
from review.models import Review, Ticket
from django.contrib import messages
# Create your views here.

class ReviewView(View):

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
        print("before self.form01 ")
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
                return redirect('create_review')
            else:
                for error in errors:
                    messages.add_message(request, messages.ERROR, error)
                return redirect('create_review')
