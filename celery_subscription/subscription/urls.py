from django.urls import path
from .views import SubscriptionView, SuccessSubscriptionView


urlpatterns = [
    path('subscription/form/', SubscriptionView.as_view()),
    path('success/', SuccessSubscriptionView.as_view(), name='success')
]
