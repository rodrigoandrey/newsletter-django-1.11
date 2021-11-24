from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView
from django.contrib import messages
from letter.models import Subscribers, News
from letter.forms import SubscribersForm


# Home View
class HomeTemplateView(TemplateView):
    template_name = 'letter/index.html'


class NewsTemplateView(ListView):
    template_name = 'letter/news.html'
    model = News
    queryset = News.objects.all()
    context_object_name = 'news'


# Registro da newsletter
def subscriber_register(request):
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Inscrição realizada com sucesso.', extra_tags='sucesso')
            return redirect('/newsletter')
    else:
        messages.info(request, 'Preencha os campos para realizar o cadastro.', extra_tags='infomarcao')
        form = SubscribersForm()

    context = {
        'form': form,
    }
    return render(request, 'letter/newsletter.html', context)


# Listagem dos subscribers
@login_required
@staff_member_required
def subscriber_view(request):
    subscribers = Subscribers.objects.all().order_by('-id').filter(status=True)
    # email_list = subscribers.values_list('email', flat=True)
    paginate_by = Paginator(subscribers, 6)
    page_number = request.GET.get('page', 1)
    try:
        page = paginate_by.page(page_number)
    except EmptyPage:
        page = paginate_by.page(1)

    context = {
        'subscribers': page,
        'page_obj': page,
    }

    return render(request, 'letter/subscribers.html', context)
