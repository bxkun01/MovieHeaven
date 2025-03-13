from django.urls import path
from .import views
from .views import (MovieListView,MovieDetailView,
                    FolderCreateView,FolderListview,
                    FolderDetailView
                )

urlpatterns=[
    path('', views.home, name='home'),
    path('films/', MovieListView.as_view(), name='film_list'),
    path('film/<int:pk>/', MovieDetailView.as_view(), name='film_detail'),
    path('search/',views.search,name='film-search'),
    path('delete-comment/<str:pk>/', views.commentdelete, name='delete-comment'),
    path('folder-create/',FolderCreateView.as_view(),name='folder-create'),
    path('lists/',FolderListview.as_view(),name='lists'),
    path('<str:user>/list/<slug:slug>',FolderDetailView.as_view(),name='folder-detail'),
    path('list/<slug:slug>/delete/', views.folderdelete, name='list-delete'),
    path('add-to-list/',views.addtolist,name='add-to-list'),

]