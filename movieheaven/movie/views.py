from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Movie

def home(request):
    return render(request, 'movie/home.html')

class MovieListView(ListView):
    model= Movie
    template_name='movie/film_list.html'
    context_object_name= 'films'
    
def search(request):
    searched = request.GET.get('searched', '')
    if searched:
        films = Movie.objects.filter(title__icontains=searched)
    else:
        films = []
    return render(request, 'movie/film_search.html', {'films': films})

class MovieDetailView(DetailView):
    model=Movie

def comment(request):
    if request.method=="POST":
        comment= request.POST.get('comment','')

    return render(request,'movie/movie_detail.html',{'comment':comment})
