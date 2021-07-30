from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import news,achievements
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


class NewsCreateView(LoginRequiredMixin,CreateView):
    model= news
    fields=['title','content','date','image','status']
    def form_valid(self,form):
        return super().form_valid(form)

class NewsUpdateView(LoginRequiredMixin,UpdateView):
    model= news
    fields=['title','content','date','image','status']
    def form_valid(self,form):
        return super().form_valid(form)



class NewsDetailView(DetailView):
    model= news

class AchievementsCreateView(LoginRequiredMixin,CreateView):
    model= achievements
    fields=['title','content','date','image','status']
    def form_valid(self,form):
        return super().form_valid(form)


def home(request):
    return render(request,'home/index.html')


def base(request):
    return render(request,'home/base.html')

def course(request):
    return render(request,'home/course.html')

def about(request):
    return render(request,'home/about.html')


def vision(request):
    return render(request,'home/vision.html')

    
def gallery(request):
    return render(request,'home/gallery.html')



def contact(request):
    return render(request,'home/contact.html')
    


class NewsListView(ListView):
 
    queryset = news.objects.filter(status='True')
   
    template_name = 'home/home.html'
    context_object_name='news'
    # order new to old
    ordering=['-date']


def NewsList(request):
   context = {
       'news' : news.objects.filter(status='True'),
       'news1' : news.objects.filter(status='False'),

   }
   return render(request,'home/home.html',context)

class achListView(ListView):
    model= achievements
    template_name = 'home/achieve.html'
    context_object_name='achieve'
    # order new to old
    ordering=['-date']