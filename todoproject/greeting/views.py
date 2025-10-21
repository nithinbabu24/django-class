from django.shortcuts import render
from .forms import LoginForm

def greeting(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            return render(request, 'form-data.html', {'email': email})
    else:
        form = LoginForm()

    return render(request, 'index.html', {'form': form})
