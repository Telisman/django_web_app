from django.forms import ModelForm
from chores.models import ChoresPost
from django import forms


class AddChoresForm(ModelForm):
    class Meta:
        model = ChoresPost
        fields = ('name', 'bio', 'category', 'budget', 'user_of_post', 'date', 'post_image')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'budget': forms.NumberInput(attrs={'min': '0', 'class': 'form-control'}),
            'user_of_post': forms.TextInput(
                attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
            'post_image': forms.FileInput(attrs={'class': 'form-control'}),

        }
