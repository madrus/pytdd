from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from lists.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = "A new list item"

        response = home_page(request)
        actual_html = response.content.decode()
        self.assertIn("A new list item", actual_html)
        # expected_html = render_to_string( # Django < v1.8
        #     'home.html',
        #     {"new_item_text": "A new list item"}
        # )
        expected_html = render_to_string( # Django >= v1.8
            'home.html',
            {"new_item_text": "A new list item"},
            request=request
        )
        self.assertEqual(expected_html, actual_html)


    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        # expected_html = render_to_string('home.html') # Django < v1.8
        expected_html = render_to_string('home.html', request=request) # Django >= v1.8
        self.assertEqual(expected_html, response.content.decode())
