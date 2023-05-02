from django.views.generic import TemplateView
from django.shortcuts import render
from django.views import View
from review.models import Ticket, Review, UserFollows
from itertools import chain
from django.db.models import CharField, Value, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
class HomeView(TemplateView):
    template_name = 'review/home.html'

    def get(self, request):
        # users i follow
        myusers = UserFollows.objects.filter(user=self.request.user)

        # users who follow me
        follusers = UserFollows.objects.filter(followed_user=self.request.user)

        # reviews from users i follow , who follow me and my reviews
        reviews = Review.objects.select_related("ticket").filter(Q(user=self.request.user) |
                                                                  Q(user__in=myusers.values_list('followed_user', flat=True)) |
                                                                  Q(user__in=follusers.values_list('user', flat=True)))
        reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

        # reviews from users i follow , who follow me and my reviews without reviews
        tickets = Ticket.objects.filter(Q(user=self.request.user) |
                                      Q(user__in=myusers.values_list('followed_user', flat=True)) |
                                      Q(user__in=follusers.values_list('user', flat=True))).exclude(id__in=reviews.values_list('ticket', flat=True))


        tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

        post_list = sorted(
            chain(reviews, tickets),
            key=lambda instance: instance.time_created,
            reverse=True
        )
        page = request.GET.get('page', 1)
        paginator = Paginator(post_list, 2)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        return render(request,
                      self.template_name,
                      context={"title": "Votre flux", "ask": "Demander une critique","create": "Créer une critique",
                               "update": "Ajouter une critique",
                       "posts": posts, 'loop_times': range(0, 5)})
