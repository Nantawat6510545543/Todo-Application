from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from todo_app.models import Todo


@login_required
def todo_list_view(request):
    if request.method == 'POST':
        todo_id = request.POST.get('todo_id')
        new_status = request.POST.get('status')

        if todo_id and new_status:
            todo = Todo.objects.filter(pk=todo_id, user=request.user).first()
            if todo:
                todo.status = new_status
                todo.save()

        return redirect('todo:todo_list')

    todos = Todo.objects.filter(user=request.user).order_by('-created_at')
    status_choices = Todo.STATUS_CHOICES
    return render(request, 'todo/todo_list.html', {
        'todos': todos,
        'status_choices': status_choices,
    })
