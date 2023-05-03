from django.shortcuts import render
from django.views import View
from review.models import Ticket, Review
from itertools import chain
from django.db.models import CharField, Value
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
class PostsView(View):
    template_name = 'review/posts.html'

    def get(self, request):
        reviews = Review.objects.select_related("ticket").filter(user=self.request.user)
        reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

        tickets = Ticket.objects.filter(user=self.request.user).exclude(
            id__in=reviews.values_list('ticket', flat=True))
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
                      context={"title": "Vos Posts", "update": "Modifier", "delete": "supprimer",
                               "posts": posts, 'loop_times': range(0, 5)})
