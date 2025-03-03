from django.urls import path
from .import views
from .views import MovieListView,MovieDetailView

urlpatterns=[
    path('', views.home, name='home'),
    path('films/', MovieListView.as_view(), name='film_list'),
    path('film/<int:pk>/', MovieDetailView.as_view(), name='film_detail'),
    path('search/',views.search,name='film-search'),
]