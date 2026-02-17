from django.shortcuts import render, redirect
from django.contrib.auth import authenticate ,login as auth_login
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        p_name = request.POST.get('username')
        p_password = request.POST.get('password')

        user_obj = authenticate(request, username=p_name, password=p_password)

        if user_obj is not None:
            auth_login(request, user_obj)
            messages.success(request, 'mrhba biiik')
            return redirect('home')
        else:
            messages.error(request, "Username ou password invalide")
            
    return render(request, 'login.html')


def creatAcc(request):

    if request.method == 'POST':
        p_usernam=request.POST.get('username')
        p_email=request.POST.get('email')
        p_password=request.POST.get('password')
        p_conf_pass=request.POST.get('password_confirm')
        if User.objects.filter(username=p_usernam).exists():
            messages.error(request, "utilisateure est dégà exist")
            return render(request, 'Register.html')
        if p_password==p_conf_pass:
            new_user = User.objects.create_user(username=p_usernam,email=p_email, password=p_password)
            messages.success(request, "Compte créé avec succès !")
            return redirect('login')
        else:
            messages.error(request, "Les mots de passe ne correspondent pas !")
            return render(request,'Register.html')
                
    return render(request, 'Register.html')














