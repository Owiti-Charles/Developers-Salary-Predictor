from django.urls import path

from .views import home

app_name = "predictor"

urlpatterns = [path("", view=home, name="home")]
