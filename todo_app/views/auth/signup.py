from django.shortcuts import render, redirect
from django.contrib.auth import login
from todo_app.forms import SignUpForm


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('todo:index')
    else:
        form = SignUpForm()
    return render(request, 'todo/auth/signup.html', {'form': form})
