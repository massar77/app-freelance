from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'login.html')

def signin(request):
    return render(request, 'signin.html')

def account(request):
    return render(request, 'account.html')