from django.urls import path

from . import views

urlpatterns = [
    # I think the "" means the root of this app (polls)
    path("", views.index, name="index")
]