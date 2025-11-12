from django.test import TestCase
import datetime
from catalog.forms import RenewBookForm

# Тесты для формы продления книги
class RenewBookFormTest(TestCase):

    def test_renew_form_date_field_label(self):
        # Проверка метки поля даты
        form = RenewBookForm()
        self.assertTrue(
            form.fields['renewal_date'].label is None or
            form.fields['renewal_date'].label == 'renewal date'
        )

    def test_renew_form_date_field_help_text(self):
        # Проверка подсказки поля
        form = RenewBookForm()
        self.assertEqual(
            form.fields['renewal_date'].help_text,
            'Enter a date between now and 4 weeks (default 3).'
        )

    def test_renew_form_date_in_past(self):
        # Дата в прошлом - невалидна
        date = datetime.date.today() - datetime.timedelta(days=1)
        form = RenewBookForm(data={'renewal_date': date})
        self.assertFalse(form.is_valid())

    def test_renew_form_date_too_far_in_future(self):
        # Дата больше 4 недель - невалидна
        date = datetime.date.today() + datetime.timedelta(weeks=4) + datetime.timedelta(days=1)
        form = RenewBookForm(data={'renewal_date': date})
        self.assertFalse(form.is_valid())

    def test_renew_form_date_today(self):
        # Сегодняшняя дата - валидна
        date = datetime.date.today()
        form = RenewBookForm(data={'renewal_date': date})
        self.assertTrue(form.is_valid())

    def test_renew_form_date_max(self):
        # Дата ровно через 4 недели - валидна
        date = datetime.date.today() + datetime.timedelta(weeks=4)
        form = RenewBookForm(data={'renewal_date': date})
        self.assertTrue(form.is_valid())