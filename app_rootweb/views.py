
from django.http import JsonResponse
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required


def home(request):
    # return JsonResponse('ok', safe=False)
    return render(request, "index_.html", {})

@login_required(login_url='/')
def index(request):
    # return JsonResponse('ok', safe=False)
    
    # return render(request, "index.html", {})
    return render(request, "index_.html", {})

def login(request):
    return redirect('login')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })