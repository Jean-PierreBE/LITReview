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
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name='connexion/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', connexion.views.SignupView.as_view(), name='signup'),
    path('home/posts', login_required(review.views.PostsView.as_view()), name='posts'),
    path('home/abonnements', login_required(review.views.UserFollowsView.as_view()), name='abonnements'),
    path('home/create_review/<int:ticket_pk>', login_required(review.views.review_create.as_view()),
         name='create_review'),
    path('home/abonnements/<int:pk>', login_required(review.views.follow_user_delete.as_view()),
         name='delete_abonnements'),
    path('home/create_own_review', login_required(review.views.OwnReview_create.as_view()), name='create_own_review'),
    path('home/delete_review/<int:pk>', login_required(review.views.review_delete.as_view()), name='delete_review'),
    path('home/create_ticket', login_required(review.views.CreateTicketView.as_view()), name='create_ticket'),
    path('home/posts/delete_ticket/<int:pk>', login_required(review.views.ticket_delete.as_view()),
         name='delete_ticket'),
    path('home/posts/edit_ticket/<int:pk>', login_required(review.views.ticket_update.as_view()), name='edit_ticket'),
    path('home/posts/edit_review/<int:pk>', login_required(review.views.review_update.as_view()), name='edit_review'),
    path('home/', login_required(review.views.HomeView.as_view()), name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
