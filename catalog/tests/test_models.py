from django.test import TestCase
from catalog.models import Author

class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Создание тестового автора для всех методов
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        # Проверка метки поля имени
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_date_of_death_label(self):
        # Проверка метки поля даты смерти
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEqual(field_label, 'died')

    def test_first_name_max_length(self):
        # Проверка максимальной длины фамилии
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        # Проверка строкового представления
        author = Author.objects.get(id=1)
        expected = f'{author.last_name}, {author.first_name}'
        self.assertEqual(str(author), expected)

    def test_get_absolute_url(self):
        # Проверка URL автора
        author = Author.objects.get(id=1)
        self.assertEqual(author.get_absolute_url(), '/catalog/author/1/')