from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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

    return render(request, 'review/crud_ticket.html')

