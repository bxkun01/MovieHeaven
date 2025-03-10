from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView, CreateView
from .models import Movie,Comment, MovieFolder
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'movie/home.html')

class MovieListView(ListView):
    model= Movie
    template_name='movie/film_list.html'
    context_object_name= 'films'
    
def search(request):
    searched = request.GET.get('searched', '')
    words= searched.split()


    if searched:
        films = Movie.objects.filter(title__iexact=words)
    else:
        films = []
    return render(request, 'movie/film_search.html', {'films': films})

class MovieDetailView(DetailView):
    model=Movie

    def post(self, request, *args, **kwargs):
        movie = self.get_object()  # Get the movie object using the pk passed in the URL
        if request.method == 'POST':
            comment_text = request.POST.get('comment', '')
            if comment_text:
                Comment.objects.create(user=request.user, text=comment_text, movie=movie)
        return redirect('film_detail', pk=movie.pk)

@login_required
def commentdelete(request, pk):
    comment= Comment.objects.get(id=pk)
    if request.user == comment.user:
        comment.delete()
        return redirect(request.META.get('HTTP_REFERER', '/'))
    

class FolderCreateView(CreateView):
    model = MovieFolder
    fields= ['title']
    success_url= reverse_lazy('lists')

    def form_valid(self, form):
        form.instance.user= self.request.user
        return super().form_valid(form)

class FolderListview(ListView):
    model= MovieFolder
    context_object_name='folders'




    

    