from django.views.generic import DetailView, ListView

from users.models import User
from django.http.response import HttpResponse
from django.shortcuts import render

class IndexView(ListView):
    template_name = 'users/index.html'
    context_object_name = 'user_list'
    
    def get_queryset(self):
        return User.objects.all()


def detail(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'users/detail.html', {'user' : user})