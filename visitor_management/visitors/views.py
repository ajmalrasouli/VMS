# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Visitor
from .forms import UserRegisterForm
from crispy_bootstrap5.bootstrap5 import FloatingField
from django.contrib.auth import logout

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')

class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return redirect('home')

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def visitor_list(request):
    visitors = Visitor.objects.all()
    return render(request, 'visitors/visitor_list.html', {'visitors': visitors})

@login_required
def sign_out_visitor(request, visitor_id):
    visitor = get_object_or_404(Visitor, id=visitor_id)
    visitor.sign_out_time = timezone.now()
    visitor.save()
    return redirect('dashboard')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'visitors/register.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'registration/logout.html')

@login_required
def dashboard(request):
    total_visitors = Visitor.objects.count()
    active_visitors = Visitor.objects.filter(sign_out_time__isnull=True).count()
    total_sign_outs = Visitor.objects.filter(sign_out_time__isnull=False).count()

    context = {
        'total_visitors': total_visitors,
        'active_visitors': active_visitors,
        'total_sign_outs': total_sign_outs,
        'visitors': Visitor.objects.all(),
    }

    return render(request, 'visitors/dashboard.html', context)

@login_required
def profile(request):
    user = request.user
    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        
    }
    return render(request, 'visitors/profile.html', context)

def logout_view(request):
    logout(request)
    return redirect('login') 