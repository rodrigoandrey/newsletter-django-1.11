from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.forms import CustomUserCreationForm
from django.views.generic import TemplateView

class UserProfile(TemplateView):
    template_name = 'accounts/profile.html'

def user_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso.')
            return redirect('/accounts/login')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/register.html', context)
