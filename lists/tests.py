import unittest
from superlists.settings import TEMPLATES
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
# from django.test import TestCase

from lists.views import home_page


class HomePageTest(unittest.TestCase):

    def test_settings(self):
        print TEMPLATES[0]
        pass


    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


    def test_home_page_returns_correct_html(self):
        # SETUP
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = "A new list item"
        # EXERCISE
        response = home_page(request)
        actual_html = response.content.decode()
        # expected_html = render_to_string( # Django < v1.8
        #     'home.html',
        #     {"new_item_text": "A new list item"}
        # )
        expected_html = render_to_string( # Django >= v1.8
            'home.html',
            {"new_item_text": "A new list item"},
            request=request
        )
        # ASSERT
        self.assertIn("A new list item", actual_html)
        self.assertEqual(actual_html, expected_html)


    # def test_home_page_can_save_a_POST_request(self):
    #     # SETUP
    #     request = HttpRequest()
    #     request.method = 'POST'
    #     request.POST['item_text'] = "A new list item"
    #     # EXERCISE
    #     response = home_page(request)
    #     actual_html = response.content.decode()
    #     # ASSERT
    #     self.assertIn("A new list item", actual_html)
