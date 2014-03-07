# -*- coding: utf-8 -*-
"""Tests."""
from django.test import TestCase
from forms.{{ cookiecutter.channel_code }} import SubscriptionForm


class {{ cookiecutter.repo_name }}Test(TestCase):
    def test_render_as_p(self):
        form = SubscriptionForm()
        self.assertIsInstance(form.as_p(), unicode)

    def test_form_validation_ok(self):
        form = SubscriptionForm({'customer_id': '1ABC234'})
        self.assertTrue(form.is_valid())

    def test_form_validation_nok(self):
        form = SubscriptionForm()
        self.assertFalse(form.is_valid())
