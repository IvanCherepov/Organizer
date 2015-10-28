from django.forms import ModelForm

from .models import Link, List


class LinkForm(ModelForm):
    class Meta:
        model = Link
        exclude = ('date_created', 'date_modified', 'owner')

class ListForm(ModelForm):
    class Meta:
        model = List
        exclude = ('date_created', 'date_modified', 'owner')