from django import forms
from models import NameRecord


class NameForm(forms.ModelForm):
    class Meta:
        model = NameRecord
        fields = ('name', 'sex', 'description', 'groups', 'zodiacs')

