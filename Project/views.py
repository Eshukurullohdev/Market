from django.shortcuts import render,redirect, get_object_or_404
from .models import Tovar, Qoshimcha_Tovar
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import HttpResponse


def purchase(request):
    return HttpResponse("Purchase Page")

def base(request):
    return render(request, 'base.html')


def nav(request):
    return render(request, "navigation.html")

def home(request):
    tovarlar = Tovar.objects.all()
    return render(request, "home.html", {"tovarlar": tovarlar})


def topshirish(request):
    return render(request, "topshirish.html")

def Sotuvchi(request):
    return render (request, "sotuvchi.html")

def sotuvchi_bolish(request):
    return render(request, "sotuvchi_bolish.html")

def footer(request):
    return render(request, "footer.html")


def savat(request):
    return render(request, "savat.html")



def savol_javob(request):
    return render(request, "savol.html")


def qoshimcha_tovar(request):
    qoshimcha_tovar = Qoshimcha_Tovar.objects.all()
    return render(request, "qoshimcha.html", {"qoshimcha_tovar": qoshimcha_tovar})


def register(request):
    if request.method == "POST":
        username = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        
        if password != confirm_password:
            messages.error(request, "Parol bir hil emas")
            return render(request, "register.html")
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Bu email allaqochon mavjud")
            
        user = User.objects.create_user(email=email, username=username, password=password, )
        user.save()
        
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Siz muvafaqiyatli Royhatan otdiz")
            return render(request, "home.html")

        messages.error(request, "Authenticationda xatolik bor")
        return render(request, "register.html")
            
    return render(request, "register.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Siz muvafaqiyatli tizimga kirdiz")
            return redirect("home")
        
    return render(request, "login.html")


def Detail_Tovar(request, pk):
    tovarlar = get_object_or_404(Tovar, pk=pk)
    return render(request, "detail_tovar.html", {"tovarlar": tovarlar})


def logout(request):
    auth_logout(request)
    return render(request, "logout.html")
    return redirect("home")


def admin_dashboard(request):
    user = User.objects.all()
    return render(request, "admin_dashboard.html", {"user": user})



