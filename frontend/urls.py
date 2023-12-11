

from django.urls import path

from frontend import views

urlpatterns = [

    path("", views.landingFunction, name="landing"),
    path("", views.landingStudioSpaceFunction, name="landing-studio-space"),
    path("", views.landingListenFunction, name="landing-listen"),
    path("", views.contactUs, name="contact-us"),


]