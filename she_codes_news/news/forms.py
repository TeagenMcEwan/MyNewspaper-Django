from django import forms 
from django.forms import ModelForm
from .models import NewsStory
# from django.contrib.auth.mixins import LoginRequiredMixin

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'content', 'image']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class':'form',
                    'placeholder': 'Text Here',
                }
            ),
            'pub_date': forms.DateInput(
                format=('%m/%d/%Y'),
                attrs={
                    'class':'form',
                    'placeholder': 'Select a date',
                    'type': 'date',
                }
            ),
            'content': forms.TextInput(
                attrs={
                    'class':'form',
                    'placeholder': 'Start your story here',
                }
            ),
            'image': forms.TextInput(
                attrs={
                    'class':'form',
                    'placeholder': 'Insert URL',
                }
            ),
            'button': forms.TextInput(
                attrs={
                    'class':'form',
                    'placeholder': 'Submit',
                }
            ),
        }