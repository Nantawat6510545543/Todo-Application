from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from todo_app.forms import TodoForm

@login_required
def add_todo_view(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo:todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo/todos/add_todo.html', {'form': form})
