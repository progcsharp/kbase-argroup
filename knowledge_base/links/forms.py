from django import forms

from links.models import Tag


class LinkForm(forms.Form):
    name = forms.CharField(label='Поиск', max_length=2500)
    tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())

