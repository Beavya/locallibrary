from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre, Language
from django.views import generic


def index(request):
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()
    num_genres = Genre.objects.count()
    num_language = Language.objects.count()

    keyword = 'Harry'
    num_books_with_keyword = Book.objects.filter(title__icontains=keyword).count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_language': num_language,
        'num_books_with_keyword': num_books_with_keyword,
        'keyword': keyword,
    }

    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author