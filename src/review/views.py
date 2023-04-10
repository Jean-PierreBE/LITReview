from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from review.forms import TicketForm

# Create your views here.
@login_required
def home(request):

    return render(request, 'review/home.html')

@login_required
def posts(request):

    return render(request, 'review/posts.html')

@login_required
def abonnements(request):

    return render(request, 'review/abonnements.html')

@login_required
def crud_review(request):

    return render(request, 'review/crud_review.html')

@login_required
def crud_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid:
            ticket_form = form.save(commit=False)
            ticket_form.user = request.user
            ticket_form.save()
        return HttpResponseRedirect()
    else:
        form = TicketForm()

    return render(request, 'review/crud_ticket.html', {"form": form})

