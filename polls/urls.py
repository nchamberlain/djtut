from django.urls import path

from . import views

app_name= "polls"
urlpatterns = [
    # the "" here means the root of this app (polls) not of overall website
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]