from django import forms 
from django.forms import ModelForm
from .models import NewsStory


class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'author', 'pub_date', 'content', 'image']
        widgets = {
            'pub_date': forms.DateInput(
                format=('%m/%d/%Y'),
                attrs={
                    'class':'form',
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'class':'form',
                    'placeholder': 'Text Here'
                }
            ),
             'author': forms.TextInput(
                attrs={
                    'class':'form',
                    'placeholder': 'Text Here'
                }
            ),
            'content': forms.TextInput(
                attrs={
                    'class':'form',
                    'placeholder': 'Text Here'
                }
            ),
            'image': forms.TextInput(
                attrs={
                    'class':'form',
                    'placeholder': 'Text Here'
                }
            ),
            'button': forms.TextInput(
                attrs={
                    'class':'form',
                    'placeholder': 'Text Here'
                }
            ),
        }