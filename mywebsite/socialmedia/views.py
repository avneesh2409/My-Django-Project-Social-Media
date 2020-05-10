from django.shortcuts import render,redirect
import datetime 
# Create your views here.

def index(request):
    now = datetime.datetime.now()
    context =  {
        'date':now
    }
    return render(request, 'index.html',context)

from .forms import PostForm

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})

from django.utils import timezone
from .models import Hero,Student,Post
from django.shortcuts import get_object_or_404

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})

def post_detail(request,pk):
    context = {
        'post':Post.objects.get(pk=pk)
    }
    return render(request,'post_detail.html',context)

from rest_framework import viewsets
from .myapi.serializers import HeroSerializer,StudentSerializer



class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('name')
    serializer_class = StudentSerializer


from django.views import View
from django.http import HttpResponse

class HelloWorldView(View):

    def get(self, request, *args, **kwargs):
        print(args,kwargs)
        return HttpResponse('Hello, World!')

from django.views.generic.base import TemplateView
class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_students'] = Student.objects.all()[:5]
        return context


from django.views.generic import ListView

class HeroList(ListView):
    model = Hero
    template_name = 'hero_list.html'

