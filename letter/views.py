from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from letter.models import Subscribers
from letter.forms import SubscribersForm


class SubscribersCreateView(CreateView):
    model = Subscribers
    form_class = SubscribersForm
    template_name = 'letter/index.html'

    def form_valid(self, form):
        subscriber = Subscribers(**form.cleaned_data)
        subscriber.save()
        messages.success(self.request, 'Inscrição realiziada com sucesso')
        return redirect('/newsletter')


class SubscribersListView(LoginRequiredMixin, ListView):
    model = Subscribers
    template_name = 'letter/subscribers.html'
    context_object_name = 'subscribers'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(status=True)

        return qs

