from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from todo_app.models import Todo

@login_required
def todo_list_view(request):
    todos = Todo.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'todo/todo_list.html', {'todos': todos})

