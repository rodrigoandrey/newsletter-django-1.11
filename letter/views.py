from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from letter.models import Subscribers
from letter.forms import SubscribersForm


# Home View
class HomeTemplateView(TemplateView):
    template_name = 'letter/index.html'


# Registro da newsletter
def subscriber_register(request):
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Inscrição realizada com sucesso.')
            return redirect('/newsletter')
    else:
        form = SubscribersForm()

    context = {
        'form': form,
    }
    return render(request, 'letter/newsletter.html', context)


# Listagem dos subscribers
class SubscribersListView(LoginRequiredMixin, ListView):
    model = Subscribers
    template_name = 'letter/subscribers.html'
    context_object_name = 'subscribers'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(status=True)

        return qs
