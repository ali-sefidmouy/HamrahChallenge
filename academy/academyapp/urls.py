from django.urls import path

from .views import SumView


app_name = "academyapp"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('academy/', SumView),
]