from django.urls import path

from django.conf import settings
from .views import index_view, signup_view, login_view, logout_view, todo_list_view, add_todo_view
from django.conf.urls.static import static

app_name = 'todo'

urlpatterns = [
    path('', index_view, name='index'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('todos/', todo_list_view, name='todo_list'),
    path('add/', add_todo_view, name='add_todo'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
