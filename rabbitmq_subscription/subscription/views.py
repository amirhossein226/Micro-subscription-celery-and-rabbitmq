from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

from .forms import SubscriptionForm
# Create your views here.


class SubscriptionView(FormView):
    template_name = 'subscription/subscription_form.html'
    success_url = 'success/'
    form_class = SubscriptionForm

    def form_valid(self, form):
        form.call_match()
        return super().form_valid(form)


class SuccessSubscriptionView(TemplateView):
    template_name = 'subscription/success.html'
