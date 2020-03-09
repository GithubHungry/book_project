from django.urls import path

from . import views

urlpatterns = [
	path('', views.BookListView.as_view(), name='book_list'),
	path('filter/', views.FilterBooksView.as_view(), name='filter'),
	path('<slug:slug>/', views.BookDetailView.as_view(), name='book_detail'),
	path('review/<int:book_id>/', views.AddReview.as_view(), name='book_review'),
	path('author/<str:slug>/', views.AuthorView.as_view(), name='author_detail'),
]
