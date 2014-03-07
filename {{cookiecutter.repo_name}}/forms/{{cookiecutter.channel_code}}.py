"""Subscription forms."""
import floppyforms as forms
from django.utils.translation import ugettext_lazy as _


class SubscriptionForm(forms.Form):
    customer_id = forms.CharField(
        label=_('Customer ID'),
        max_length=20,
        help_text=_('The Customer ID appears on your bills.'),
    )
