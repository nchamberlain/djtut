from django.urls import path
from polls.views import AboutView
from . import views

app_name= "polls"
urlpatterns = [
    # the "" here means the root of this app (polls) not of overall website
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("polls/about/", AboutView.as_view()),
]