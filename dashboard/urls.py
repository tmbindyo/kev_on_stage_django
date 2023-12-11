from django.urls import path

from dashboard import views

urlpatterns = [

    path("login", views.login_view, name="dashboard-login"),

]