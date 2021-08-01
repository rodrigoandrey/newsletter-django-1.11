from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import CreateView, ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from letter.models import Subscribers
from letter.forms import SubscribersForm


class HomeTemplateView(TemplateView):
    template_name = 'letter/index.html'


class SubscribersCreateView(CreateView):
    model = Subscribers
    form_class = SubscribersForm
    template_name = 'letter/newsletter.html'

    def form_valid(self, form):
        subscriber = Subscribers(**form.cleaned_data)
        subscriber.save()
        messages.success(self.request, 'Inscrição realizada com sucesso')
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



