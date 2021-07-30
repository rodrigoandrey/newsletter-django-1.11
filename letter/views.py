from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy
from letter.models import NewsLetter
from letter.forms import NewsLetterForm


class NewsLetterView(CreateView):
    model = NewsLetter
    form_class = NewsLetterForm
    template_name = 'letter/index.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        subscriber = NewsLetter(**form.cleaned_data)
        subscriber.save()
        messages.success(self.request, 'Inscrição realiziada com sucesso')
