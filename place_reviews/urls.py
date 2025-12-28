"""
URL configuration for place_reviews project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from users.views import RegisterView
from reviews.views import AddReviewView
from places.views import SearchPlaceView, PlaceDetailView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('review/', AddReviewView.as_view()),
    path('search/', SearchPlaceView.as_view()),
    path('place/<int:place_id>/', PlaceDetailView.as_view()),
]
