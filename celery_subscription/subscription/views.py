from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from .forms import SubscriptionForm
# Create your views here.


class SubscriptionView(FormView):
    template_name = 'subscription/subscription_form.html'
    form_class = SubscriptionForm
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        form.match_address()
        return super().form_valid(form)


class SuccessSubscriptionView(TemplateView):
    template_name = 'subscription/success.html'
