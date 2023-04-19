"""WebReview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
import review.views
import connexion.views
from django.views import View
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
            template_name='connexion/login.html',
            redirect_authenticated_user=True),
             name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', connexion.views.SignupView.as_view(), name='signup'),
    path('home/posts', login_required(review.views.PostsView.as_view()), name='posts'),
    path('home/abonnements', login_required(review.views.UserFollowsView.as_view(title01="Suivre d'autres utilisateurs", action01 = "envoyer",
                                                                  title02="Abonnements",
                                                                  title03="Abonnés")),
         name='abonnements'),
    path('home/create_review', login_required(review.views.ReviewView.as_view()), name='create_review'),
    path('home/create_ticket', login_required(review.views.CreateTicketView.as_view(title="Créer un ticket", action = "créer")), name='create_ticket'),
    path('home/', login_required(review.views.HomeView.as_view()), name='home'),
]
