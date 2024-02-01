from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'slug']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-box title-info-size'}),
            'content': forms.Textarea(attrs={'class': 'input-box content-info-size', 'cols': 50, 'rows': 10}),
            'slug': forms.TextInput(attrs={'class ': 'input-box title-info-size'})
        }

