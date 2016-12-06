from django import forms
from npnbase.models import NameRecord


class NameForm(forms.ModelForm):
    class Meta:
        model = NameRecord
        fields = ('name', 'sex', 'description', 'groups', 'zodiacs')


