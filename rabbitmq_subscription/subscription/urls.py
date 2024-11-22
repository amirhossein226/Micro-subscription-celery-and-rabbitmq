from django.urls import path
from .views import SubscriptionView, SuccessSubscriptionView

urlpatterns = [
    path('subscription/', SubscriptionView.as_view()),
    path('subscription/success/', SuccessSubscriptionView.as_view())
]
