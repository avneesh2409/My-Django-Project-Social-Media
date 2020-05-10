from django.shortcuts import render
import datetime 
# Create your views here.

def index(request):
    now = datetime.datetime.now()
    context =  {
        'date':now
    }
    return render(request, 'index.html',context)

from rest_framework import viewsets
from .myapi.serializers import HeroSerializer,StudentSerializer
from .models import Hero,Student


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

