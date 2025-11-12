from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),

    # Списки объектов
    path('books/', views.BookListView.as_view(), name='books'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),

    # Детальные страницы объектов
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),

    # Страницы взятых книг
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('borrowed/', views.AllBorrowedBooksListView.as_view(), name='all-borrowed'),

    # Действия с книгами
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),

    # CRUD для авторов
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),

    # CRUD для книг
    path('book/create/', views.BookCreate.as_view(), name='book-create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),
]