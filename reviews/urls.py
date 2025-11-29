from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReviewView.as_view()),
    path("thank/", views.ThankYou.as_view()),
    path("listreviews/", views.ListReviews.as_view()),
    path('listreviews/liked_id', views.AddLikeView.as_view()),
    path("listreviews/<int:pk>", views.SingleReview.as_view()),
]
