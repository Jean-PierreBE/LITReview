from django.shortcuts import render
from django.views import View
from review.models import Ticket, Review
from itertools import chain
from django.db.models import CharField, Value

# Create your views here.
class PostsView(View):
    template_name = 'review/posts.html'

    def get(self, request):
        posts = Review.objects.select_related("ticket").filter(user=self.request.user)
        print(str(posts.query))
        for post in posts:
            print("post.image " + str(post.ticket.image))
            print("post.description " + str(post.ticket.description))
            print("post.title " + str(post.ticket.title))


        return render(request,
                      self.template_name,
                      {"title": "Vos Posts", "update": "Modifier", "delete": "supprimer",
                       "posts": posts})

