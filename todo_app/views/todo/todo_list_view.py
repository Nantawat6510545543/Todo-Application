from django.contrib.auth.decorators import login_required

@login_required
def todo_list_view(request):
    pass
