from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# Inline для отображения экземпляров книг в админке книг
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

# Inline для отображения книг в админке авторов
class BooksInline(admin.TabularInline):
    model = Book
    extra = 0

# Настройки админки для модели Author
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]

# Регистрация модели Book с декоратором
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

    # Кастомный метод для отображения жанров
    def display_genre(self, obj):
        return ', '.join([genre.name for genre in obj.genre.all()[:3]])

    display_genre.short_description = 'Genre'

# Регистрация модели BookInstance с декоратором
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    # Группировка полей в форме редактирования
    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )

# Регистрация моделей в админке
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(Language)